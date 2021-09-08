import unittest

from translator import french_to_english , english_to_french


class TestMyModule(unittest.TestCase):
    def test_null_french(self):
        self.assertEqual(french_to_english(""),"")
    def test_null_english(self):
        self.assertEqual(english_to_french(""),"")
    def test_hello_english(self):
       self.assertEqual(french_to_english("Bonjour"),"Hello")
    def test_hello_french(self):
       self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__ == '__main__':
    unittest.main()    