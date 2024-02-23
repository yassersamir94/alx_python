#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
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

    # Execute a SQL query
    cur.execute("SELECT * FROM states ORDER BY id")

    # Fetch all the rows using fetchall() method
    rows = cur.fetchall()

    # Print the result
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
