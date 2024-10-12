# Project ArXiv Citation Network

## Overview

This project involved the analysis of the ArXiv citation network.

## Usage

### Data Preparation

To prepare the data, run the following command:

```bash
python3 cite_parser.py
```

This will generate csv files for the nodes and edges of the citation network.

### Neo4j Database

To load the data into a Neo4j database, run the following command:

```bash
python3 neo4j_data_importer.py
```

This will load the data from the csv files into a Neo4j database.

> [!NOTE]
> If it takes too long to load the data, you can change the number of random samples in the `cite_parser.py` file (`N_SAMPLES` variable).

## Data

The data was extracted from: [https://github.com/mattbierbaum/arxiv-public-datasets/releases/tag/v0.2.0](https://github.com/mattbierbaum/arxiv-public-datasets/releases/tag/v0.2.0). More exactly, we'll use the file "internal-references-v0.2.0-2019-03-01.json.gz", which contains the list of papers and their references, all papers using their arXiv IDs.
