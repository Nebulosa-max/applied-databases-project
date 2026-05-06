from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")


def get_neo4j_driver():
    return GraphDatabase.driver(
        NEO4J_URI,
        auth=(NEO4J_USER, NEO4J_PASSWORD)
    )


def test_neo4j_connection():
    try:
        driver = get_neo4j_driver()

        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run("RETURN 'Neo4j connection successful!' AS message")
            record = result.single()
            print(record["message"])

        driver.close()

    except Exception as e:
        print("Neo4j connection failed.")
        print(e)


if __name__ == "__main__":
    test_neo4j_connection()