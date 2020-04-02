import sys, os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json


engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

Base = automap_base()
Base.prepare(engine, reflect=True)
Books = Base.classes.books

def bookpagehelper(bookid):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "iGZG0s5CY0rwO3Muq7Nw0g", "isbns": bookid})
    book = session.query(Books).filter_by(isbn=bookid).first()
    r = json.dumps(res.json())
    loaded_r = json.loads(r)
    return (book.__dict__, loaded_r)