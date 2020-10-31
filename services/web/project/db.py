#https://github.com/pallets/flask-sqlalchemy
#https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
DATABASE_URI ='postgresql://milton:cuenca@db:5432/soluciones_reinas'
engine = create_engine(DATABASE_URI, convert_unicode=True)
Base = declarative_base() 
Session.configure(bind=engine)
Session = Session(autocommit=False)

