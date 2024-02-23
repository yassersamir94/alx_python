#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is passed
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query
    sql_query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the SQL query
    cursor.execute(sql_query, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Close cursor and database connection
    cursor.close()
    db.close()

    # Print the cities
    for city in cities:
        print(city[0], end=", ")

    print()  # Add newline at the end
