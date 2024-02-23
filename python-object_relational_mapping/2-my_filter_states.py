#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL server running on localhost at port 3306
    and displays all values in the states table where name matches the argument.
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

    # Execute a SQL query to select states based on user input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(query, (sys.argv[4],))

    # Fetch all the rows using fetchall() method
    rows = cur.fetchall()

    # Print the result
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
