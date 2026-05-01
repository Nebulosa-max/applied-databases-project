"""Attendee service module.

This file contains functionality related to attendees stored
in the MySQL database.
"""

from db.mysql_connection import get_mysql_connection


def view_attendees_by_company():
    """Retrieve and display attendees belonging to a selected company."""
    connection = get_mysql_connection()

    if connection is None:
        print("Could not connect to the MySQL database.")
        return

    try:
        cursor = connection.cursor()

        company_id = input("Enter company ID: ").strip()

        if not company_id.isdigit() or int(company_id) <= 0:
            print("Invalid company ID. Please enter a number greater than 0.")
            return

        company_query = """
            SELECT company_name
            FROM companies
            WHERE company_id = %s;
        """
        cursor.execute(company_query, (company_id,))
        company = cursor.fetchone()

        if company is None:
            print("Company ID does not exist.")
            return

        attendee_query = """
            SELECT
                attendee_id,
                attendee_name,
                dob,
                gender
            FROM attendees
            WHERE company_id = %s
            ORDER BY attendee_name;
        """
        cursor.execute(attendee_query, (company_id,))
        attendees = cursor.fetchall()

        company_name = company[0]

        print(f"\nAttendees for {company_name}")
        print("-" * 60)

        if not attendees:
            print(f"No attendees found for {company_name}.")
            return

        for attendee in attendees:
            attendee_id, attendee_name, dob, gender = attendee
            print(f"Attendee ID: {attendee_id}")
            print(f"Name: {attendee_name}")
            print(f"DOB: {dob}")
            print(f"Gender: {gender}")
            print("-" * 60)

    except Exception as error:
        print(f"Error retrieving attendees by company: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def add_new_attendee():
    """Add a new attendee to the MySQL database."""
    connection = get_mysql_connection()

    if connection is None:
        print("Could not connect to the MySQL database.")
        return

    try:
        cursor = connection.cursor()

        attendee_id = input("Enter attendee ID: ").strip()
        attendee_name = input("Enter attendee name: ").strip()
        dob = input("Enter date of birth (YYYY-MM-DD): ").strip()
        gender = input("Enter gender: ").strip()
        company_id = input("Enter company ID: ").strip()

        if not attendee_id.isdigit() or int(attendee_id) <= 0:
            print("Invalid attendee ID. Please enter a number greater than 0.")
            return

        if not attendee_name:
            print("Attendee name cannot be empty.")
            return

        if not company_id.isdigit() or int(company_id) <= 0:
            print("Invalid company ID. Please enter a number greater than 0.")
            return

        check_attendee_query = """
            SELECT attendee_id
            FROM attendees
            WHERE attendee_id = %s;
        """
        cursor.execute(check_attendee_query, (attendee_id,))
        existing_attendee = cursor.fetchone()

        if existing_attendee is not None:
            print("Attendee ID already exists.")
            return

        check_company_query = """
            SELECT company_id
            FROM companies
            WHERE company_id = %s;
        """
        cursor.execute(check_company_query, (company_id,))
        existing_company = cursor.fetchone()

        if existing_company is None:
            print("Company ID does not exist.")
            return

        insert_query = """
            INSERT INTO attendees (
                attendee_id,
                attendee_name,
                dob,
                gender,
                company_id
            )
            VALUES (%s, %s, %s, %s, %s);
        """

        values = (
            attendee_id,
            attendee_name,
            dob,
            gender,
            company_id
        )

        cursor.execute(insert_query, values)
        connection.commit()

        print("Attendee successfully added.")

    except Exception as error:
        print(f"Error adding attendee: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
