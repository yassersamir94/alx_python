#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL server running on localhost at port 3306
    and displays all values in the cities table sorted by cities.id.
    """

    # Connect to MySQL database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object using cursor() method
    cur = conn.cursor()

    # Construct the SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id"

    # Execute the SQL query
    cur.execute(query)

    # Fetch all the rows using fetchall() method
    rows = cur.fetchall()

    # Print the result
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
