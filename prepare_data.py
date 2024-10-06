import os
import json
import random
import pandas as pd

# Set random seed for reproducibility
random.seed(42)

# Constants
N_SAMPLES = 20000
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
        return [json.loads(line) for line in file]


def sample_dict_data(data, n_samples):
    """Samples a given number of entries from the dictionary."""
    sampled_keys = random.sample(list(data.keys()), n_samples)
    return {k: data[k] for k in sampled_keys if data[k]}


def save_dataframe(df: pd.DataFrame, file_path: str, message: str):
    """Saves a DataFrame to a CSV file and prints a message."""
    df.to_csv(file_path, encoding="utf-8", index=False)
    print(f"{message}: {len(df)} entries saved to {os.path.basename(file_path)}")


def create_citation_df(citation_data):
    """Creates a DataFrame for citations."""
    citations = [(key, ref) for key in citation_data for ref in citation_data[key]]
    df = pd.DataFrame(
        citations, columns=["main_paper", "referenced_paper"]
    ).drop_duplicates()
    intersecting_papers = set(df["main_paper"]).intersection(df["referenced_paper"])
    return df[df["main_paper"].isin(intersecting_papers)]


def create_metadata_df(metadata):
    """Creates a metadata DataFrame and applies transformations."""
    metadata_df = pd.DataFrame(metadata)[
        ["id", "title", "report-no", "doi", "submitter", "abstract_md5"]
    ]
    metadata_df.rename(columns={"id": "idAxv"}, inplace=True)
    metadata_df["idAxv"] = metadata_df["idAxv"].apply(lambda x: f"x{x}")
    metadata_df["title"] = metadata_df["title"].str.replace("\n", "")
    return metadata_df


def extract_field_entries(info, field, separator=", ", clean=True, is_list=False):
    """Extracts entries for a given field (authors or categories)."""
    entries, paper_entries = [], []
    for entry in info:
        items = entry[field][0] if is_list else entry[field]
        items = items.replace(" and ", separator).split(separator)
        if clean:
            items = [
                item.strip().replace(",", "").replace('"', "").replace("\n", "")
                for item in items
            ]
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
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Process and save citations
    citation_data = load_json(CITATION_JSON)
    sampled_data = sample_dict_data(citation_data, N_SAMPLES)
    citations_df = create_citation_df(sampled_data)
    save_dataframe(citations_df, CITATIONS_FILE, "Citations")

    # Process and save metadata
    metadata = load_metadata(METADATA_JSON)
    process_metadata(metadata, METADATA_FILE)

    # Extract and save authors
    authors, paper_authors = extract_field_entries(metadata, "authors", is_list=True)
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
