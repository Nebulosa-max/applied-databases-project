# Applied Databases Project

Final project for the Applied Databases module.

This project is a Python-based conference management application that uses both a relational database and a graph database:

- MySQL
- Neo4j

The application is run from the command line using `main.py`.

---

## Project Overview

The purpose of this project is to demonstrate the use of multiple database technologies in one Python application.

MySQL is used to store structured conference data such as attendees, speakers, sessions and rooms.

Neo4j is used to store and query relationships between attendees, allowing the application to represent attendee connections as a graph.

---

## Main Features

The application allows the user to:

1. View speakers and sessions
2. View attendees by company
3. Add a new attendee
4. View connected attendees
5. Add attendee connections
6. View rooms
7. Exit the application

---

## Technologies Used

- Python 3
- MySQL
- Neo4j Aura
- mysql-connector-python
- neo4j Python driver
- python-dotenv
- Git and GitHub

---

## Project Structure

```text
applied-databases-project/
│
├── db/
│   ├── mysql_connection.py
│   ├── neo4j_connection.py
│   └── README.md
│
├── docs/
│   ├── project_notes.md
│   └── README.md
│
├── services/
│   ├── attendee_service.py
│   ├── connection_service.py
│   ├── room_service.py
│   ├── speaker_service.py
│   └── README.md
│
├── utils/
│   └── menu.py
│
├── main.py
├── seed_neo4j.py
├── requirements.txt
├── innovation.md
├── Gitlink.txt
├── .gitignore
└── README.md
```

---

## Database Design

### MySQL

MySQL is used for the relational part of the project.

It stores structured conference data such as:

- attendees
- companies
- speakers
- sessions
- rooms

The MySQL connection is handled in:

```text
db/mysql_connection.py
```

The application reads MySQL credentials from environment variables stored in a `.env` file.

The `.env` file is not included in the repository for security reasons.

Example MySQL environment variables:

```env
MYSQL_HOST=localhost
MYSQL_USER=conference_user
MYSQL_PASSWORD=conference_pass
MYSQL_DATABASE=conference_db
```

---

### Neo4j

Neo4j is used for the graph database part of the project.

It stores attendee connection data, where attendees are represented as nodes and their relationships are represented as graph relationships.

The Neo4j connection is handled in:

```text
db/neo4j_connection.py
```

The Neo4j seed file is:

```text
seed_neo4j.py
```

This file creates test attendee nodes and relationships in the Neo4j database.

Example Neo4j environment variables:

```env
NEO4J_URI=neo4j+s://your-database-uri
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password
NEO4J_DATABASE=neo4j
```

The real Neo4j credentials are stored locally in the `.env` file and are not committed to GitHub.

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Nebulosa-max/applied-databases-project.git
cd applied-databases-project
```

---

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

---

### 3. Create a `.env` file

Create a `.env` file in the root of the project.

Add the MySQL and Neo4j credentials to the file.

Example:

```env
MYSQL_HOST=localhost
MYSQL_USER=conference_user
MYSQL_PASSWORD=conference_pass
MYSQL_DATABASE=conference_db

NEO4J_URI=neo4j+s://your-database-uri
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password
NEO4J_DATABASE=neo4j
```

The `.env` file is included in `.gitignore` and should not be committed.

---

### 4. Seed the Neo4j database

Before testing the Neo4j attendee connection features, run:

```bash
python seed_neo4j.py
```

This creates sample attendee connection data in Neo4j.

---

### 5. Run the application

```bash
python main.py
```

The application will display the main menu:

```text
1. View Speakers & Sessions
2. View Attendees by Company
3. Add New Attendee
4. View Connected Attendees
5. Add Attendee Connection
6. View Rooms
x. Exit application
```

---

## Menu Options

### Option 1: View Speakers & Sessions

Displays speaker and session information stored in MySQL.

### Option 2: View Attendees by Company

Displays attendee information grouped or filtered by company using MySQL data.

### Option 3: Add New Attendee

Allows the user to add a new attendee to the MySQL database.

### Option 4: View Connected Attendees

Displays attendee connections stored in Neo4j.

### Option 5: Add Attendee Connection

Allows the user to add a relationship between two attendees in Neo4j.

### Option 6: View Rooms

Displays room information from the MySQL database.

---

## Security Notes

Sensitive files are excluded from the repository using `.gitignore`.

The following files should not be committed:

```text
.env
Neo4j-*.txt
__pycache__/
```

Database credentials are stored locally in the `.env` file only.

---

## GitHub Repository

The project repository is available at:

```text
https://github.com/Nebulosa-max/applied-databases-project
```

---

## Author

Sophia Godoy

Applied Databases Project  
Atlantic Technological University