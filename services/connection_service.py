from db.neo4j_connection import get_neo4j_driver
from dotenv import load_dotenv
import os

load_dotenv()

NEO4J_DATABASE = os.getenv("NEO4J_DATABASE")


def view_connected_attendees():
    driver = get_neo4j_driver()

    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run("""
                MATCH (a:Attendee)-[r:CONNECTED_TO]->(b:Attendee)
                RETURN a.name AS attendee,
                       b.name AS connected_attendee,
                       r.reason AS reason
                ORDER BY a.name
            """)

            connections = list(result)

            if not connections:
                print("\nNo attendee connections found.")
                return

            print("\nConnected Attendees")
            print("-" * 60)

            for record in connections:
                print(f"{record['attendee']} is connected to {record['connected_attendee']}")
                print(f"Reason: {record['reason']}")
                print("-" * 60)

    except Exception as e:
        print("\nError retrieving connected attendees from Neo4j.")
        print(e)

    finally:
        driver.close()