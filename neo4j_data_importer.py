import os
import pandas as pd
from neo4j import GraphDatabase
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

# Constants
URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")
MAX_CONNECTION_POOL_SIZE = 5

CSV_DIR = "output"
CSV_FILES = {
    "authors": f"{CSV_DIR}/authors.csv",
    "categories": f"{CSV_DIR}/categories.csv",
    "papers": f"{CSV_DIR}/metadata.csv",
    "paper_authors": f"{CSV_DIR}/paper_authors.csv",
    "paper_categories": f"{CSV_DIR}/paper_categories.csv",
    "citations": f"{CSV_DIR}/citations_network.csv",
}

# SAMPLE_SIZES = {"papers": 200, "authors": 50, "categories": 50}


def create_nodes(session, csv_path, label, field_map, **kwargs):
    """Creates nodes from CSV file with optional sampling."""
    try:
        nodes_df = pd.read_csv(csv_path, dtype=str)
        n_samples = kwargs.get("n_samples")
        if n_samples:
            nodes_df = nodes_df.sample(n_samples)

        for _, row in tqdm(
            nodes_df.iterrows(), total=len(nodes_df), desc=f"Creating {label} nodes"
        ):
            properties = {key: row.iloc[field_map[key]] for key in field_map}
            query = (
                f"CREATE (n:{label} {{"
                + ", ".join([f"{key}: ${key}" for key in properties])
                + "})"
            )
            session.run(query, **properties)
        return nodes_df
    except Exception as e:
        print(f"Error creating {label} nodes from {csv_path}: {e}")


def create_rels(session, start_df, end_df, csv_path, **kwargs):
    """Creates relationships between nodes if both exist."""
    try:
        rels_df = pd.read_csv(csv_path, dtype=str)
        rels_df = rels_df[
            rels_df[kwargs["start_field"]].isin(start_df[kwargs["start_field"]])
            & rels_df[kwargs["end_field"]].isin(end_df[kwargs["end_field"]])
        ]

        for _, row in tqdm(
            rels_df.iterrows(),
            total=len(rels_df),
            desc=f"Creating {kwargs['rel_type']} relationships",
        ):
            query = (
                f"MATCH (a:{kwargs['start_lbl']} {{{kwargs['start_field']}: $start_field}}), "
                f"(b:{kwargs['end_lbl']} {{{kwargs['end_field']}: $end_field}}) "
                f"CREATE (a)-[:{kwargs['rel_type']}]->(b)"
            )
            session.run(
                query,
                start_field=row[kwargs["start_field"]],
                end_field=row[kwargs["end_field"]],
            )
    except Exception as e:
        print(f"Error creating {kwargs['rel_type']} relationships from {csv_path}: {e}")


def create_cites_rels(session, df, csv_path):
    """Creates CITES relationships between papers."""
    try:
        cites_df = pd.read_csv(csv_path, dtype=str)
        print(cites_df.iloc[0])
        cites_df = cites_df[
            cites_df["main_paper"].isin(df["idAxv"])
            & cites_df["referenced_paper"].isin(df["idAxv"])
        ]

        for _, row in tqdm(
            cites_df.iterrows(),
            total=len(cites_df),
            desc="Creating CITES relationships",
        ):
            query = (
                "MATCH (a:Paper { idAxv: $main_paper }), "
                "(b:Paper { idAxv: $referenced_paper }) "
                "CREATE (a)-[:CITES]->(b)"
            )
            session.run(
                query,
                main_paper=row["main_paper"],
                referenced_paper=row["referenced_paper"],
            )
    except Exception as e:
        print(f"Error creating CITES relationships from {csv_path}: {e}")


def main():
    # Create a Neo4j driver and session
    driver = GraphDatabase.driver(
        URI, auth=AUTH, max_connection_pool_size=MAX_CONNECTION_POOL_SIZE
    )
    session = driver.session(database=DATABASE)

    # Field mappings for nodes
    field_mappings = {
        "paper": {
            "idAxv": 0,
            "title": 1,
            "report_no": 2,
            "doi": 3,
            "submitter": 4,
            "abstract_md5": 5,
            "authors": 6,
        },
        "author": {"author": 0},
        "category": {"category": 0},
    }

    # Create nodes for authors, categories, and papers
    # authors_df = create_nodes(
    #     session,
    #     CSV_FILES["authors"],
    #     "Author",
    #     field_mappings["author"],
    #     # n_samples=SAMPLE_SIZES["authors"],
    # )
    categories_df = create_nodes(
        session,
        CSV_FILES["categories"],
        "Category",
        field_mappings["category"],
        # n_samples=SAMPLE_SIZES["categories"],
    )
    papers_df = create_nodes(
        session,
        CSV_FILES["papers"],
        "Paper",
        field_mappings["paper"],
        # n_samples=SAMPLE_SIZES["papers"],
    )

    # Create relationships between papers, authors, and categories
    # create_rels(
    #     session,
    #     papers_df,
    #     authors_df,
    #     CSV_FILES["paper_authors"],
    #     rel_type="AUTHORED",
    #     start_lbl="Paper",
    #     end_lbl="Author",
    #     start_field="idAxv",
    #     end_field="author",
    # )
    create_rels(
        session,
        papers_df,
        categories_df,
        CSV_FILES["paper_categories"],
        rel_type="CATEGORIZED",
        start_lbl="Paper",
        end_lbl="Category",
        start_field="idAxv",
        end_field="category",
    )
    create_cites_rels(session, papers_df, CSV_FILES["citations"])

    # Close the session and driver
    session.close()
    driver.close()


if __name__ == "__main__":
    main()
