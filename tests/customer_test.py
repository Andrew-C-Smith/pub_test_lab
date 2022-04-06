import unittest

from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self): # NEW
      self.customer = Customer("Andrew", 50) # NEW

    def test_customer_has_name(self): # NEW
        self.assertEqual("Andrew", self.customer.name) # NEW