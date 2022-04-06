# tests/pub_test.py
import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer


class TestPub(unittest.TestCase):

    def setUp(self): # NEW
      self.pub = Pub("The Chanter", 100.00) # NEW

    def test_pub_has_name(self): # NEW
        self.assertEqual("The Chanter", self.pub.name) # NEW
# tests/pub_test.py


    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till) # NEW


# tests/pub_test.py

    def increase_till(self, amount):
        self.till += amount

# tests/pub_test.py


