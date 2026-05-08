# Project Notes

## Project Overview

This document records the planning, design decisions, implementation notes, database choices, security considerations, and innovation rationale for the `applied-databases-project`.

The main purpose of this project was to build a working conference management application supported by two different database technologies:

- **MySQL** for structured relational data.
- **Neo4j** for graph-based relationships and recommendations.

While the README focuses on how to set up and run the application, this document explains the reasoning behind the design and implementation choices.

---

## Project Goal

The goal of the project was to design and implement a database-driven application for managing conference information. The application allows users to interact with conference-related data through a command-line interface.

The system includes functionality for managing and viewing:

- Speakers
- Sessions
- Attendees
- Topics
- Recommendations based on graph relationships

The project demonstrates how relational and graph databases can be used together in one application, with each database selected according to the type of data it handles best.

---

## Database Design Rationale

### MySQL

MySQL was chosen to store structured data where relationships are clearly defined and tabular.

This includes information such as:

- Speaker details
- Session details
- Attendee details
- Topic details
- Connections between sessions, speakers, and attendees

MySQL is suitable for this part of the project because it supports:

- Relational structure
- Primary keys and foreign keys
- Data integrity
- SQL queries
- Clear organisation of structured information

The relational database supports the core operational part of the application.

---

### Neo4j

Neo4j was chosen for relationship-based data and recommendation logic.

Graph databases are useful when the main focus is not only the data itself, but also the connections between pieces of data.

Neo4j was used to model relationships such as:

- Attendees interested in topics
- Sessions connected to topics
- Recommendations based on shared interests
- Connections between conference participants and content

This makes Neo4j suitable for demonstrating more innovative functionality, such as suggesting relevant sessions to attendees based on their interests.

---

## Why Two Databases Were Used

The project uses both MySQL and Neo4j because each database type solves a different problem.

MySQL is better for structured, transactional, tabular data.

Neo4j is better for exploring relationships and patterns between entities.

Using both databases shows a polyglot persistence approach, where different database technologies are combined in one project to support different types of data and queries.

This design decision makes the application more realistic and demonstrates an understanding that not all data problems should be solved with the same database model.

---

## Application Structure

The application is written in Python and uses a command-line menu system.

The structure separates the project into different files and responsibilities, including:

- Main application logic
- Database connection logic
- MySQL setup and queries
- Neo4j setup and queries
- Supporting documentation

This separation improves readability and makes the project easier to maintain.

The application was designed to be simple to run while still showing clear interaction with both database systems.

---

## Implementation Notes

The application connects to MySQL and Neo4j using environment variables stored in a `.env` file.

This approach avoids hardcoding sensitive credentials directly inside the Python files.

The main program provides menu options that allow the user to run different parts of the system.

The implementation includes:

- Creating database records
- Reading existing data
- Displaying structured information
- Creating graph nodes and relationships
- Running recommendation logic using Neo4j relationships

During development, the project was tested by running the Python application locally and checking that both database systems responded correctly.

---

## Environment Variables

The project uses a `.env` file to store local database credentials.

Example variables include:

- MySQL host
- MySQL username
- MySQL password
- MySQL database name
- Neo4j URI
- Neo4j username
- Neo4j password
- Neo4j database name

The `.env` file should not be committed to GitHub if it contains real credentials.

A separate example file can be used to show the expected structure without exposing private information.

---

## Security Considerations

Several security considerations were taken into account during the project.

### Credentials

Database credentials should not be hardcoded in the Python source code.

Using a `.env` file makes the project safer and easier to configure on different machines.

### Version Control

Sensitive files such as `.env` should be excluded from GitHub using `.gitignore`.

This prevents private passwords or local configuration details from being accidentally published.

### Database Access

The database user should ideally have only the permissions required for the project.

For a college project, local development credentials may be simple, but in a production system stronger access control would be required.

### Input Handling

In a larger production system, user input should be validated carefully to reduce the risk of invalid data or injection attacks.

This project is a local command-line academic application, but the same principle still applies.

---

## Design Decisions

### Command-Line Interface

A command-line interface was used because it keeps the focus on the database logic rather than on front-end design.

This made it possible to demonstrate the database functionality clearly and directly.

### Modular Python Files

The project was organised into multiple files to avoid placing all logic into one large script.

This improves maintainability and makes the code easier to understand.

### Clear Documentation

Documentation was added to make the project easier to review, run, and understand.

The README explains setup and execution.

This project notes file explains the design thinking and implementation rationale.

---

## Innovation Rationale

The most innovative part of the project is the use of Neo4j alongside MySQL.

A basic conference application could be built using only a relational database. However, adding Neo4j allows the project to demonstrate relationship-based thinking.

For example, a recommendation system can use graph relationships to connect attendees, topics, and sessions.

This creates a more intelligent application because it can suggest relevant sessions based on interests rather than only displaying static data.

This shows how graph databases can add value when connections between entities are important.

---

## Limitations

The project was developed as a college assessment and is designed to run locally.

Some limitations include:

- The interface is command-line based rather than web-based.
- The project uses local database connections.
- The recommendation logic is simple and designed for demonstration.
- The application is not intended for production deployment.
- More advanced validation and error handling could be added in future versions.

---

## Possible Future Improvements

Future improvements could include:

- A web interface using Flask or Django
- More advanced recommendation queries in Neo4j
- Stronger validation for user input
- Improved error handling
- Automated testing
- Docker support for easier setup
- Expanded sample data
- Admin and user roles
- Exporting reports from conference data

These additions would make the project more scalable and closer to a real-world conference management system.

---

## Reflection

This project helped demonstrate the difference between relational and graph database models.

MySQL provided a reliable structure for core conference data, while Neo4j allowed relationships and recommendations to be represented more naturally.

Using both technologies in one project showed how different database systems can support different parts of the same application.

The project also reinforced the importance of documentation, environment configuration, and clean version control practices.

---

## References

- MySQL Documentation: https://dev.mysql.com/doc/
- Neo4j Documentation: https://neo4j.com/docs/
- Python Documentation: https://docs.python.org/3/
- Python Dotenv Documentation: https://pypi.org/project/python-dotenv/
- Git Documentation: https://git-scm.com/doc
