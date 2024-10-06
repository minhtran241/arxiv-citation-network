# Create Neo4j nodes and relationships, node name are the titles of the papers, attributes are the ids. Relationships are the citations (references) between the papers.
# citations_network.csv is the input file, which contains the citation information of the papers. The first column is the citing paper, the second column is the cited paper.
# infos_idd_name.csv is the input file, which contains the id and title of the papers. The first column is the id, the second column is the title.

import csv
from py2neo import Graph, Node, Relationship

graph = Graph("http://localhost:7474", username="neo4j", password="123456")
