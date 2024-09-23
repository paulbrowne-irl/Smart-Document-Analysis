import unittest
import shelve
from . import text_extract

class TestScore(unittest.TestCase):

    def test_text_extract(self):
        text_extract.read_text_from_file("test_data\\simple.txt")
    
    def test_text_extract_word(self):
        text_extract.read_text_from_file("test_data\\simple.docx")

    def test_text_extract_excel(self):
        text_extract.read_text_from_file("test_data\\simple.xlsx")        

if __name__ == '__main__':
    unittest.main()