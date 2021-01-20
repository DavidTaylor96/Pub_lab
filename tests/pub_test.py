import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drinks("beer", 3)
        self.drink_2 = Drinks("wine", 4)
        self.drink_3 = Drinks("vodka", 7)

        self.pub = Pub("The Prancing Pony", 100)

        self.pub.add_drink_to_list(self.drink_1)
        self.pub.add_drink_to_list(self.drink_2)
        self.pub.add_drink_to_list(self.drink_3)

        self.customer_1 = Customer("David", 20)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_drinks_list(self):
        self.assertEqual(3, self.pub.check_the_list())

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(self.drink_2.amount)
        self.assertEqual(104, self.pub.till)

    def test_find_drink_by_name(self):
        drink = self.pub.find_drink_by_name("vodka")
        self.assertEqual(drink, self.drink_3)
    
    def test_sell_drink_to_customer(self):
        self.pub.sell_drink_to_customer(self.customer_1, "vodka")
        self.assertEqual(107, self.pub.till)
        self.assertEqual(13, self.customer_1.wallet)        


        