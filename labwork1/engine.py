from sqlalchemy import create_engine

engine = create_engine("sqlite:///wholesale.db", echo=True, future=True)
