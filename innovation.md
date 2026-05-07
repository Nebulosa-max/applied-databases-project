# Innovation Statement

This project uses both relational and graph database technologies to manage conference data.

MySQL is used to store structured conference information, such as attendees, speakers, sessions and bookings. This is appropriate for data that fits well into tables and relationships using primary and foreign keys.

Neo4j is used to represent attendee connections. This adds a graph database element to the project and allows relationships between attendees to be stored and queried in a more natural way.

The innovation in this project is the combination of MySQL and Neo4j in one Python application. Instead of using only one database system, the project uses each database for a purpose that matches its strengths.

This design shows how different database models can work together in the same application:

- MySQL stores structured event and booking data.
- Neo4j stores and manages attendee-to-attendee connections.
- Python connects the application logic to both databases.
- The menu system allows the user to interact with both databases from one place.

This approach makes the project more flexible and demonstrates an understanding of both relational and graph database concepts.
