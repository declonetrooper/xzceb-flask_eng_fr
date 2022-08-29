from translator import *
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        with self.assertRaises(ValueError):
            french_to_english(None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")


    def test_2(self):
        with self.assertRaises(ValueError):
            english_to_french(None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")


if __name__ == '__main__':
    unittest.main()
