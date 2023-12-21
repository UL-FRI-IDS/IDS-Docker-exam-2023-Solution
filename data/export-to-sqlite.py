# 1. Connect to the postgresql database `Airline Flights`.
# 2. Select passenger data (passenger id, passenger name, contact data).
# 3. Create a new sqlite database `/data/airlines-passengers.db` containing a table `Passenger`. 
# Copy all the passenger data into the SQLite database.

import sqlite3

# 1.
import psycopg2
conn = psycopg2.connect(host="postgres", 
                        dbname="demo",
                        user="postgres", 
                        password="Geslo.DataScience.2023")
conn.autocommit = True

# 2.
data = []
cursor = conn.cursor()
query = ("""
    SELECT passenger_id, passenger_name, contact_data FROM tickets;
""")

cursor.execute(query)

for line in cursor:
  data.append((line[0], line[1], str(line[2])))

cursor.close()

# 3.

conn = sqlite3.connect('/data/airlines-passengers.db')

c = conn.cursor()

cursor = c.execute('''
    CREATE TABLE Passenger (
      passenger_id TEXT NOT NULL,
        passenger_name TEXT NOT NULL,
        contact_data TEXT
    );
''')

conn.commit()


for line in data:
  cursor = c.execute('''
    INSERT INTO Passenger (passenger_id, passenger_name, contact_data)
    VALUES (?, ?, ?)
  ''', line)

conn.commit()

conn.close()