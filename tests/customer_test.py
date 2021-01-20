import unittest
from src.customer import Customer
from src.drinks import Drinks

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer_1 = Customer("David", 20)

    def test_find_customer_name(self):
        self.assertEqual("David", self.customer_1.name)

    def test_find_wallet(self):
      self.assertEqual(20, self.customer_1.wallet)

    def test_remove_money_wallet(self):
      drink = Drinks("wine", 4)
      self.customer_1.remove_money_wallet(drink.amount)
      self.assertEqual(16, self.customer_1.wallet)