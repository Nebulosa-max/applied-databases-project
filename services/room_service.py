"""Room service module.

This file contains the functionality related to viewing rooms
stored in the MySQL database.
"""

from db.mysql_connection import get_mysql_connection


def view_rooms():
    """Retrieve and display all rooms from the MySQL database."""
    connection = get_mysql_connection()

    if connection is None:
        print("Could not connect to the MySQL database.")
        return

    try:
        cursor = connection.cursor()
        query = """
            SELECT room_id, room_name, capacity
            FROM rooms
            ORDER BY room_id;
        """
        cursor.execute(query)
        rooms = cursor.fetchall()

        if not rooms:
            print("No rooms found.")
            return

        print("\nRooms")
        print("-" * 40)

        for room in rooms:
            room_id, room_name, capacity = room
            print(f"Room ID: {room_id}")
            print(f"Room Name: {room_name}")
            print(f"Capacity: {capacity}")
            print("-" * 40)

    except Exception as error:
        print(f"Error retrieving rooms: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
