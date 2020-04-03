from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv,os

# from mytvpy.models import base

# Define variables DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME   
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base(name = 'Model')
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

@dataclass
class Book(Base):
    isbn: str
    title: str
    author: str
    year: int

    __tablename__ = 'books'
    isbn = Column(String, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    def __init__ (self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

Base.metadata.create_all(engine)

# with open('books.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print("Header")
#         else:
#             book = session.query(Book).filter_by(isbn=row["isbn"]).first()
#             if not book:
#                 book = Book(row["isbn"] , row["title"], row["author"], row["year"])
#                 session.add(book)
#             else:
#                 print("Already Present in the database")
#         session.commit()
#         line_count = line_count + 1
#     print("Loading Complete")




# session.commit()










# try:
#    connection = psycopg2.connect(user="sysadmin",
#                                   password="pynative@#29",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="postgres_db")
#    cursor = connection.cursor()

#    postgres_createtable_query = """
# CREATE TABLE books(
# id integer PRIMARY KEY,
# email text,
# name text,
# address text)
# """
#    # cur.execute()
#    
#    # postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
#    # record_to_insert = (5, 'One Plus 6', 950)
#    cursor.execute(postgres_insert_query, record_to_insert)

#    connection.commit()
#    count = cursor.rowcount
#    print (count, "Record inserted successfully into mobile table")

# except (Exception, psycopg2.Error) as error :
#     if(connection):
#         print("Failed to insert record into mobile table", error)

# finally:
#     #closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")