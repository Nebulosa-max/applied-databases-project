"""Speaker service module.

This file contains the functionality related to viewing speakers
and their sessions from the MySQL database.
"""

from db.mysql_connection import get_mysql_connection


def view_speakers_and_sessions():
    """Retrieve and display speakers and their sessions from MySQL."""
    connection = get_mysql_connection()

    if connection is None:
        print("Could not connect to the MySQL database.")
        return

    try:
        cursor = connection.cursor()

        speaker_name = input(
            "Enter full or partial speaker name, or press Enter to view all: "
        ).strip()

        query = """
            SELECT
                s.speaker_id,
                s.speaker_name,
                se.session_title,
                r.room_name
            FROM speakers s
            JOIN sessions se ON s.speaker_id = se.speaker_id
            JOIN rooms r ON se.room_id = r.room_id
        """

        values = ()

        if speaker_name:
            query += """
                WHERE s.speaker_name LIKE %s
            """
            values = (f"%{speaker_name}%",)

        query += """
            ORDER BY s.speaker_name, se.session_title;
        """

        cursor.execute(query, values)
        results = cursor.fetchall()

        if not results:
            print("No speakers or sessions found.")
            return

        print("\nSpeakers and Sessions")
        print("-" * 60)

        for row in results:
            speaker_id, speaker_name, session_title, room_name = row
            print(f"Speaker ID: {speaker_id}")
            print(f"Speaker Name: {speaker_name}")
            print(f"Session Title: {session_title}")
            print(f"Room: {room_name}")
            print("-" * 60)

    except Exception as error:
        print(f"Error retrieving speakers and sessions: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
