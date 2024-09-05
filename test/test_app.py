# test/test_app.py
import unittest
from src.app import greet
from src.utils import get_time_of_day

class TestApp(unittest.TestCase):
    def test_greet(self):
        greeting = greet('GitHub')
        time_of_day = get_time_of_day()
        self.assertIn(f'Good {time_of_day}, GitHub!', greeting)

    def test_time_of_day(self):
        time_of_day = get_time_of_day()
        self.assertIn(time_of_day, ["morning", "afternoon", "evening"])

if __name__ == '__main__':
    unittest.main()
