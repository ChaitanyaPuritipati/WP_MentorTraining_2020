import os
import unittest
from flask import Flask
import bookpage

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self):
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        
  
    # executed after each test
    def tearDown(self):
        pass
    

    ###############
    #### tests ####
    ###############

    def test_bookpage(self):
        data, ratings = bookpage.bookpagehelper("0380803267")
        self.assertEqual(data["title"],'King of Foxes')
        self.assertEqual(data["author"], 'Raymond E. Feist')
        # print(ratings['books'][0])
        self.assertEqual(ratings['books'][0]['average_rating'], '3.98')

if __name__ == "__main__":
    unittest.main()


