#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Creating a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Creating a Session
    session = Session()

    # Querying the database to fetch the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Displaying the first State object if it exists
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Closing the session
    session.close()
