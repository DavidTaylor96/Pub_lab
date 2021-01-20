import unittest

from src.drinks import Drinks

class TestDrinks(unittest.TestCase):

  def test_find_drink_name(self):
    self.drink = Drinks("wine", "Beer")
    self.assertEqual("wine", self.drink.name)
