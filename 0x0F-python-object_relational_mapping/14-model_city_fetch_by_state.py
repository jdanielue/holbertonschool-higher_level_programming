#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_city import Base, City, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    session = Session(bind=engine)

    cities_states = (session.query(City).order_by(City.id)
                            .join(State, State.id == City.state_id))
    for city in cities_states:
        print("{}: ({}) {}".format(city.states.name, city.id, city.name))
    session.close()
