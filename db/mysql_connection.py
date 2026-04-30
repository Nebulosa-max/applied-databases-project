"""MySQL database connection module.

This file contains the function used to connect the Python application
to the MySQL database.
"""

import mysql.connector
from mysql.connector import Error


def get_mysql_connection():
    """Create and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="conference_db"
        )

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"MySQL connection error: {error}")
        return None
