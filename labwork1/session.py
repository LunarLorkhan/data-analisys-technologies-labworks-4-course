from sqlalchemy.orm import scoped_session, sessionmaker

from engine import engine

session = scoped_session(sessionmaker(bind=engine))
