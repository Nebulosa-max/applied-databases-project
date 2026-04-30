"""Neo4j database connection module.

This file contains the function used to connect the Python application
to the Neo4j graph database.
"""

from neo4j import GraphDatabase


def get_neo4j_driver():
    """Create and return a Neo4j database driver."""
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "password"

    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        driver.verify_connectivity()
        return driver

    except Exception as error:
        print(f"Neo4j connection error: {error}")
        return None
