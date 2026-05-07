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
                RETURN a.id AS attendee_id,
                       a.name AS attendee_name,
                       b.id AS connected_attendee_id,
                       b.name AS connected_attendee_name,
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
                print(
                    f"{record['attendee_name']} "
                    f"(ID: {record['attendee_id']}) "
                    f"is connected to "
                    f"{record['connected_attendee_name']} "
                    f"(ID: {record['connected_attendee_id']})"
                )
                print(f"Reason: {record['reason']}")
                print("-" * 60)

    except Exception as e:
        print("\nError retrieving connected attendees from Neo4j.")
        print(e)

    finally:
        driver.close()


def add_attendee_connection():
    driver = get_neo4j_driver()

    try:
        print("\nAdd Attendee Connection")
        print("-" * 60)

        attendee_1_id = input("Enter first attendee ID: ").strip()
        attendee_1_name = input("Enter first attendee name: ").strip()

        attendee_2_id = input("Enter second attendee ID: ").strip()
        attendee_2_name = input("Enter second attendee name: ").strip()

        reason = input("Enter connection reason: ").strip()

        if not attendee_1_id or not attendee_1_name or not attendee_2_id or not attendee_2_name or not reason:
            print("\nAll fields are required.")
            return

        with driver.session(database=NEO4J_DATABASE) as session:
            session.run("""
                MERGE (a:Attendee {id: toInteger($attendee_1_id)})
                SET a.name = $attendee_1_name

                MERGE (b:Attendee {id: toInteger($attendee_2_id)})
                SET b.name = $attendee_2_name

                MERGE (a)-[r:CONNECTED_TO]->(b)
                SET r.reason = $reason
            """,
            attendee_1_id=attendee_1_id,
            attendee_1_name=attendee_1_name,
            attendee_2_id=attendee_2_id,
            attendee_2_name=attendee_2_name,
            reason=reason)

            print("\nAttendee connection added successfully!")

    except Exception as e:
        print("\nError adding attendee connection to Neo4j.")
        print(e)

    finally:
        driver.close()
