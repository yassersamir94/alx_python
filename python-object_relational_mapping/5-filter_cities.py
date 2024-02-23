#!/usr/bin/python3
"""
Lists all cities of a specific state from the database
"""

import sys
import MySQLdb

def filter_cities(username: str, password: str, database_name: str, state_name: str) -> None:
    """
    Connects to the MySQL database and retrieves all cities of the specified state.
    Prints the cities sorted by ID.
    """
    try:
        db = MySQLdb.connect(host="localhost",
                             user=username,
                             passwd=password,
                             db=database_name,
                             port=3306)

        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities \
                     JOIN states ON cities.state_id = states.id \
                     WHERE states.name = %s \
                     ORDER BY cities.id ASC", (state_name,))

        cities = cur.fetchall()
        print(", ".join(city[0] for city in cities))

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(username, password, database_name, state_name)
