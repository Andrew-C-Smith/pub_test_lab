
import unittest
from src.drinks import Drinks


class TestPub(unittest.TestCase):

    def setUp(self): # NEW
      self.Drinks = Drinks("Beer", 3.50) # NEW

    def test_drink_has_name(self): # NEW
        self.assertEqual("Beer", self.drinks.name) # NEW