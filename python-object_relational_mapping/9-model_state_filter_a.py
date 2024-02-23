#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database hbtn_0e_6_usa
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

    # Querying the database to fetch State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Displaying State objects containing 'a'
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Closing the session
    session.close()
