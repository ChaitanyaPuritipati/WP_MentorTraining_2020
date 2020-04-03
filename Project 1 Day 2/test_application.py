import unittest
import os
from flask import Flask, session, request, render_template, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, exc, desc, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_session import Session
from sqlalchemy import create_engine
from datetime import datetime
from passlib.hash import bcrypt
from application import app
from bs4 import BeautifulSoup

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        
        self.app = app.test_client()
        self.app.testing = True 
        self.assertEqual(app.debug, False)
        
  
    # executed after each test
    def tearDown(self):
        pass
    
    ########################
    #### helper methods ####
    ########################
     
    def register(self, username,email, password):
        return self.app.post('/register',data=dict(Username = username, Email=email, password = password),follow_redirects=True)
     
    def login(self, email, password):
        return self.app.post('/auth',data=dict(email=email, password=password),follow_redirects=True)
    

    ###############
    #### tests ####
    ###############

    def test_register(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_invalid_user_registration(self):
        response = self.register('FlaskIsAwesome','something@gmail.com',  'FlaskIsAwesome')
        soup = BeautifulSoup(response.data, 'html.parser')
        divalert = soup.find("div", {"class": "alert"})
        divalerttext = divalert.prettify(formatter="html")
        divalerttext = divalerttext.split("</button>")[1]
        divalerttext = divalerttext.replace("</div>", "")
        divalerttext = divalerttext.replace("\n", "")
        divalerttext = divalerttext.strip(" ")

        self.assertEqual(response.status_code, 200)
        self.assertIn('User Already exists', divalerttext)

    def test_valid_user_registration(self):
        response = self.register('Chaitanya Puritipati','thesecrets@gmail.com',  'idk')
        soup = BeautifulSoup(response.data, 'html.parser')
        divalert = soup.find("div", {"class": "alert"})
        divalerttext = divalert.prettify(formatter="html")
        divalerttext = divalerttext.split("</button>")[1]
        divalerttext = divalerttext.replace("</div>", "")
        divalerttext = divalerttext.replace("\n", "")
        divalerttext = divalerttext.strip(" ")

        self.assertEqual(response.status_code, 200)
        self.assertIn('Registration Success', divalerttext)
    
    def test_invalid_user_login(self):
        response = self.login('secretthe@gmail.com', 'pass')
        soup = BeautifulSoup(response.data, 'html.parser')
        divalert = soup.find("div", {"class": "alert"})
        divalerttext = divalert.prettify(formatter="html")
        divalerttext = divalerttext.split("</button>")[1]
        divalerttext = divalerttext.replace("</div>", "")
        divalerttext = divalerttext.replace("\n", "")
        divalerttext = divalerttext.strip(" ")
        self.assertEqual(response.status_code, 200)
        self.assertIn('User is not present. Please register to login.', divalerttext)



if __name__ == "__main__":
    unittest.main()
