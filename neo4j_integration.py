import os
import csv
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()


URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
MAX_CONNECTION_POOL_SIZE = 5

CSV_DIR = "output"
AUTHORS_FILE = f"{CSV_DIR}/authors.csv"
CATEGORIES_FILE = f"{CSV_DIR}/categories.csv"
PAPER_FILE = f"{CSV_DIR}/metadata.csv"
PAPER_AUTHORS_FILE = f"{CSV_DIR}/paper_authors.csv"
PAPER_CATEGORIES_FILE = f"{CSV_DIR}/paper_categories.csv"
CITATIONS_FILE = f"{CSV_DIR}/citations_network.csv"


def create_neo4j_driver(uri, auth, max_pool_size, encrypted=False):
    """Creates a Neo4j driver instance."""
    return GraphDatabase.driver(
        uri, auth=auth, max_connection_pool_size=max_pool_size, encrypted=encrypted
    )


def create_neo4j_session(driver, database="neo4j"):
    """Creates a session for Neo4j transactions."""
    return driver.session(database=database)


def create_nodes_from_csv(session, file_path, node_label, field_mapping):
    """Creates nodes from CSV file."""
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            fields = {field: row[idx] for field, idx in field_mapping.items()}
            query = f"CREATE (n:{node_label} {{"
            query += ", ".join([f"{field}: ${field}" for field in fields.keys()])
            query += "})"
            session.run(query, **fields)


def create_relationships_from_csv(
    session,
    file_path,
    relationship_type,
    start_label,
    end_label,
    start_id_field,
    end_id_field,
):
    """Creates relationships between nodes from CSV."""
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            query = (
                f"MATCH (a:{start_label} {{{start_id_field}: $start_id}}) "
                f"MATCH (b:{end_label} {{{end_id_field}: $end_id}}) "
                f"CREATE (a)-[:{relationship_type}]->(b)"
            )
            session.run(query, start_id=row[0], end_id=row[1])


def main():
    # Create a Neo4j driver and session
    driver = create_neo4j_driver(URI, AUTH, MAX_CONNECTION_POOL_SIZE)
    session = create_neo4j_session(driver)

    # Define field mappings for nodes
    paper_field_mapping = {"idAxv": 0, "title": 1}
    author_field_mapping = {"author": 0}
    category_field_mapping = {"category": 0}

    # Create nodes for authors, categories, and papers
    create_nodes_from_csv(session, AUTHORS_FILE, "Author", author_field_mapping)
    create_nodes_from_csv(session, CATEGORIES_FILE, "Category", category_field_mapping)
    create_nodes_from_csv(session, PAPER_FILE, "Paper", paper_field_mapping)

    # Create relationships between papers, authors, and categories
    create_relationships_from_csv(
        session, PAPER_AUTHORS_FILE, "AUTHORED", "Paper", "Author", "idAxv", "author"
    )
    create_relationships_from_csv(
        session,
        PAPER_CATEGORIES_FILE,
        "CATEGORIZED",
        "Paper",
        "Category",
        "idAxv",
        "category",
    )
    create_relationships_from_csv(
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
