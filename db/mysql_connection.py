"""MySQL database connection module.

This file contains the function used to connect the Python application
to the MySQL database.
"""

import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()


def get_mysql_connection():
    """Create and return a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE", "conference_db")
        )

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"MySQL connection error: {error}")
        return None
