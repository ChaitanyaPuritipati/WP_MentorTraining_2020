import sys, os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

Base = automap_base()
Base.prepare(engine, reflect=True)
Books = Base.classes.books

def search(query, option):
    books = []
    if option == "title":
        looking_for = '%{0}%'.format(query)
        books = session.query(Books).filter(Books.title.like(looking_for)).all()
    elif option == "author":
        looking_for = '%{0}%'.format(query)
        books = session.query(Books).filter(Books.author.like(looking_for)).all()
    elif option == "isbn":
        looking_for = '%{0}%'.format(query)
        books = session.query(Books).filter(Books.isbn.like(looking_for)).all()
    else:
        try:
            query = int(query)
        except Exception as e:
            sys.stdout.flush()
            return 'No results for your query'
        books = session.query(Books).filter_by(year=query).all()
    if(len(books) <= 0):
        return "No results for your query"
    return books