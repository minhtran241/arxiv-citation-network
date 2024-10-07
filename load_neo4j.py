import os
import csv
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()


URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
DATABASE = os.environ.get("NEO4J_DATABASE", "neo4j")
MAX_CONNECTION_POOL_SIZE = 5

CSV_DIR = "output"
AUTHORS_FILE = f"{CSV_DIR}/authors.csv"
CATEGORIES_FILE = f"{CSV_DIR}/categories.csv"
PAPER_FILE = f"{CSV_DIR}/metadata.csv"
PAPER_AUTHORS_FILE = f"{CSV_DIR}/paper_authors.csv"
PAPER_CATEGORIES_FILE = f"{CSV_DIR}/paper_categories.csv"
CITATIONS_FILE = f"{CSV_DIR}/citations_network.csv"


def create_nodes(session, csv_path, label, field_map):
    """Creates nodes from CSV file."""
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            fields = {field: row[idx] for field, idx in field_map.items()}
            query = f"CREATE (n:{label} {{"
            query += ", ".join([f"{field}: ${field}" for field in fields.keys()])
            query += "})"
            session.run(query, **fields)


def create_rels_from_csv(
    session,
    csv_path,
    rel_type,
    start_lbl,
    end_lbl,
    start_field,
    end_field,
):
    """Creates relationships between nodes from CSV."""
    with open(csv_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            query = (
                f"MATCH (a:{start_lbl} {{{start_field}: $start_value}}) "
                f"MATCH (b:{end_lbl} {{{end_field}: $end_value}}) "
                f"CREATE (a)-[:{rel_type}]->(b)"
            )
            session.run(query, start_value=row[0], end_value=row[1])


def main():
    # Create a Neo4j driver and session
    driver = GraphDatabase.driver(
        URI, auth=AUTH, max_connection_pool_size=MAX_CONNECTION_POOL_SIZE
    )
    session = driver.session(database=DATABASE)

    # Define field mappings for nodes
    paper_field_mapping = {"idAxv": 0, "title": 1}
    author_field_mapping = {"author": 0}
    category_field_mapping = {"category": 0}

    # Create nodes for authors, categories, and papers
    create_nodes(session, AUTHORS_FILE, "Author", author_field_mapping)
    create_nodes(session, CATEGORIES_FILE, "Category", category_field_mapping)
    create_nodes(session, PAPER_FILE, "Paper", paper_field_mapping)

    # Create relationships between papers, authors, and categories
    create_rels_from_csv(
        session, PAPER_AUTHORS_FILE, "AUTHORED", "Paper", "Author", "idAxv", "author"
    )
    create_rels_from_csv(
        session,
        PAPER_CATEGORIES_FILE,
        "CATEGORIZED",
        "Paper",
        "Category",
        "idAxv",
        "category",
    )
    create_rels_from_csv(
        session,
        CITATIONS_FILE,
        "CITES",
        "Paper",
        "Paper",
        "main_paper",
        "referenced_paper",
    )

    # Close the session and driver
    session.close()
    driver.close()


if __name__ == "__main__":
    main()
