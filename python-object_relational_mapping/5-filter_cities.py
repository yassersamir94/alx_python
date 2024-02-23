import sys
import MySQLdb

def filter_cities(username, password, database, state_name):
    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Prepare the SQL query
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"

    # Execute the query with state name as parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and database connection
    cursor.close()
    db.close()

    return rows

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python 5-filter_cities.py username password database state_name")
        sys.exit(1)

    # Parse command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Filter cities based on the provided state name
    cities = filter_cities(username, password, database, state_name)

    # Display results
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print("No cities found for the state:", state_name)
