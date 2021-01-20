import unittest
from src.pub import Pub
from src.drinks import Drinks

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    # def test_has_drinks(self):
    #     drink = Drinks("martini", "wine", "beer", "whiskey")
    #     self.pub.add_drinks(drink)
    #     self.assertEqual(1, self.pub.drinks())