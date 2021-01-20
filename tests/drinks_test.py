import unittest

from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
  def setUp(self):
    self.drink_1 = Drinks("beer", 3)
    self.drink_2 = Drinks("wine", 4)
    self.drink_3 = Drinks("vodka", 7)
    self.pub_list = [self.drink_1, self.drink_2, self.drink_3]


  def test_find_drink_name(self):
    self.assertEqual("wine", self.pub_list[1].name)
  
  def test_find_drink_prices(self):
    self.assertEqual(4, self.pub_list[1].amount)