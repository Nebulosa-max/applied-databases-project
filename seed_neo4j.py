from db.neo4j_connection import get_neo4j_driver
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")


def seed_connections():
    driver = get_neo4j_driver()

    with driver.session(database=NEO4J_DATABASE) as session:
        session.run("""
        MATCH (n)
        DETACH DELETE n
        """)

        session.run("""
        CREATE
        (a1:Attendee {id: 1, name: 'Alice Johnson'}),
        (a2:Attendee {id: 2, name: 'Brian Smith'}),
        (a3:Attendee {id: 3, name: 'Carla Mendes'}),
        (a4:Attendee {id: 4, name: 'Daniel O’Brien'}),
        (a5:Attendee {id: 5, name: 'Emma Walsh'}),

        (a1)-[:CONNECTED_TO {reason: 'Same company'}]->(a2),
        (a1)-[:CONNECTED_TO {reason: 'Attended same session'}]->(a3),
        (a2)-[:CONNECTED_TO {reason: 'Networking event'}]->(a4),
        (a3)-[:CONNECTED_TO {reason: 'Shared speaker interest'}]->(a5)
        """)

    driver.close()
    print("Neo4j test data created successfully!")


if __name__ == "__main__":
    seed_connections()