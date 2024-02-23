import MySQLdb
import sys

def get_cities(username, password, database, state_name):
    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database)

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

    return cities

if __name__ == "__main__":
    # Check if correct number of arguments is passed
    if len(sys.argv) != 5:
        print("Usage: python3 5-filter_cities.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Get cities for the given state
    cities = get_cities(username, password, database, state_name)

    # Check if cities are found
    if cities:
        # Print the cities
        print(", ".join(city[0] for city in cities))
    else:
        print(f"No cities found for the state: {state_name}")
