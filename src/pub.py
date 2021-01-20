class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []



    def check_the_list(self):
        return len(self.drinks)
     
    def add_drink_to_list(self, drink):
        self.drinks.append(drink)

    # add money till
    def add_money_to_till(self, amount):
        self.till += amount
    
    def find_drink_by_name(self, drink_name_to_find):
        for drink in self.drinks:
            if drink_name_to_find == drink.name:
                return drink


    def sell_drink_to_customer(self, customer, drink_name):
        drink_to_sell = self.find_drink_by_name(drink_name)
        customer.remove_money_wallet(drink_to_sell.amount)
        self.add_money_to_till(drink_to_sell.amount)

# Customer should buy the Drink from Pub ----- (Make this in customer)

# reduct the money in the wallet(we have this method already)
# add the money to the till (we have this method already)