#!/usr/bin/python3
"""
A script that lists all State objects that contains an a from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    just_a = session.query(State).filter(State.name.like('%a%'))
    for i in just_a:
        print("{}: {}".format(i.id, i.name))
    session.close()
