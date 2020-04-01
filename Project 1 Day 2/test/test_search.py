import unittest 
from search import *

class TestSearch(unittest.TestCase):
    
    def test_search_author(self):
        query = "abcde"
        option = "author"
        result = search(query, option)
        self.assertEqual(result, "No results for your query")
    def test_search_title(self):
        query = "abcde"
        option = "title"
        result = search(query, option)
        self.assertEqual(result, "No results for your query")
    def test_search_isbn(self):
        query = "abcde"
        option = "isbn"
        result = search(query, option)
        self.assertEqual(result, "No results for your query")
    def test_search_author_valid(self):
        query = "Raymond E. Feist"
        option = "author"
        result = search(query, option)
        for vals in result:
            self.assertEqual(vals.author, query)
    def test_search_title_valid(self):
        query = "Aztec"
        option = "title"
        result = search(query, option)
        self.assertEqual(result[0].title, query)
    def test_search_isbn_valid(self):
        query = "080213825X"
        option = "isbn"
        result = search(query, option)
        self.assertEqual(result[0].isbn, query)
    def test_search_year(self):
        query = "080213825X"
        option = "year"
        result = search(query, option)
        self.assertEqual(result, "No results for your query")
    def test_search_year_valid(self):
        query = 1995
        option = "year"
        result = search(query, option)
        for vals in result:
            self.assertEqual(vals.year, query)
    
if __name__ == '__main__':
    unittest.main() 