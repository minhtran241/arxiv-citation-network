import os
import json
import pandas as pd


# Constants
CITATION_JSON = "data/internal-references-pdftotext.json"
METADATA_JSON = "data/oai-arxiv-metadata-hash-abstracts-2019-03-01.json"
OUTPUT_DIR = "output"
CITATIONS_FILE = f"{OUTPUT_DIR}/citations_network.csv"
METADATA_FILE = f"{OUTPUT_DIR}/metadata.csv"
AUTHORS_FILE = f"{OUTPUT_DIR}/authors.csv"
PAPER_AUTHORS_FILE = f"{OUTPUT_DIR}/paper_authors.csv"
CATEGORIES_FILE = f"{OUTPUT_DIR}/categories.csv"
PAPER_CATEGORIES_FILE = f"{OUTPUT_DIR}/paper_categories.csv"


# Utility functions
def load_json(file_path):
    """Loads JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)


def load_metadata(file_path):
    """Loads metadata JSON lines and converts to a list."""
    with open(file_path, "r") as file:
        metadata = [json.loads(line) for line in file]
    return metadata[:4000]


def save_dataframe(df: pd.DataFrame, file_path: str, message: str):
    """Saves a DataFrame to a CSV file and prints a message."""
    df.to_csv(file_path, encoding="utf-8", index=False)
    print(f"{message}: {len(df)} entries saved to {os.path.basename(file_path)}")


def create_citation_df(citation_data):
    """Creates a DataFrame for citations."""
    citations = [(key, ref) for key in citation_data for ref in citation_data[key]]
    df = pd.DataFrame(
        citations, columns=["main_paper", "referenced_paper"]
    ).drop_duplicates(keep=False, inplace=False)
    intersecting_papers = set(df["main_paper"]).intersection(df["referenced_paper"])
    return df[df["main_paper"].isin(intersecting_papers)]


def create_metadata_df(metadata):
    """Creates a metadata DataFrame and applies transformations."""
    metadata_df = pd.DataFrame(metadata)[
        ["id", "title", "report-no", "doi", "submitter", "abstract_md5", "authors"]
    ]
    metadata_df = metadata_df.drop_duplicates()
    metadata_df.rename(columns={"id": "idAxv"}, inplace=True)
    # metadata_df["idAxv"] = metadata_df["idAxv"].apply(lambda x: f"x{x}")
    metadata_df["title"] = metadata_df["title"].str.replace("\n", "")
    return metadata_df


def extract_field_entries(info, field, separator=", ", clean=True, is_list=False):
    """Extracts entries for a given field (authors or categories)."""
    entries, paper_entries = [], []
    for entry in info:
        items = entry[field][0] if is_list else entry[field]
        # print(items)
        items = (
            items.replace(" and ", separator)
            .replace(", and ", separator)
            .split(separator)
        )
        if clean:
            items = [
                item.strip('"')
                .replace(",", "")
                .replace('"', "")
                .replace("\n", "")
                .replace("'", "")
                for item in items
            ]
            # some have the pattern "Haibin Zhao (1) and Haibin Zhao (2)" so we need to remove the number
            items = [item.split(" (")[0] for item in items]
            # some have the pattern "(1) Haibin Zhao" so we need to remove the number
            items = [item.split(") ")[-1] for item in items]
        entries.extend(items)
        paper_entries.extend([(entry["id"], item) for item in items])
    return entries, paper_entries


def save_extracted_data(data, columns, file_path, message):
    """Saves extracted data (authors, categories) to a CSV."""
    df = pd.DataFrame(set(data), columns=columns)
    save_dataframe(df, file_path, message)


def save_paper_data(paper_data, columns, file_path, message):
    """Saves paper-specific data (authors, categories) to a CSV."""
    df = pd.DataFrame(paper_data, columns=columns)
    save_dataframe(df, file_path, message)


def process_metadata(metadata, output_file):
    """Processes metadata and saves it as a CSV."""
    metadata_df = create_metadata_df(metadata)
    save_dataframe(metadata_df, output_file, "Metadata")


# Main workflow
def main():
    # Ask the user if they want to remove the existing files or not if they exist already
    if os.path.exists(OUTPUT_DIR):
        remove = input(
            "Output directory already exists. Do you want to remove it? (y/n): "
        )
        if remove.lower() == "y":
            os.system(f"rm -rf {OUTPUT_DIR}")
        else:
            print("Exiting...")
            return

    # Create the output directory
    os.makedirs(OUTPUT_DIR)

    # Process and save citations
    citation_data = load_json(CITATION_JSON)
    citations_df = create_citation_df(citation_data)
    # save_dataframe(citations_df, CITATIONS_FILE, "Citations")

    # Process and save metadata
    metadata = load_metadata(METADATA_JSON)
    # process_metadata(metadata, METADATA_FILE)

    # Only save citations for papers that are in the metadata
    citations_df = citations_df[
        citations_df["main_paper"].isin([entry["id"] for entry in metadata])
    ]
    citations_df = citations_df[
        citations_df["referenced_paper"].isin([entry["id"] for entry in metadata])
    ]

    # Get about 300 papers with citations to each other
    metadata = [
        entry
        for entry in metadata
        if entry["id"] in set(citations_df["main_paper"])
        or entry["id"] in set(citations_df["referenced_paper"])
    ]

    process_metadata(metadata, METADATA_FILE)

    # Save the citations with only the papers that are in the metadata
    save_dataframe(citations_df, CITATIONS_FILE, "Citations")

    # Extract and save authors
    authors, paper_authors = extract_field_entries(metadata, "authors")

    save_extracted_data(authors, ["author"], AUTHORS_FILE, "Authors")
    save_paper_data(
        paper_authors, ["idAxv", "author"], PAPER_AUTHORS_FILE, "Paper Authors"
    )

    # Extract and save categories
    categories, paper_categories = extract_field_entries(
        metadata, "categories", separator=" ", clean=False, is_list=True
    )
    save_extracted_data(categories, ["category"], CATEGORIES_FILE, "Categories")
    save_paper_data(
        paper_categories,
        ["idAxv", "category"],
        PAPER_CATEGORIES_FILE,
        "Paper Categories",
    )


if __name__ == "__main__":
    main()
