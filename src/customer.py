class Customer:

  def __init__(self, name, wallet):
    self.name = name
    self.wallet = wallet

  # Buy a drink from the pub
  def buy_a_drink(self, buy):
    for drink in buy.price:
      self.wallet - drink
      return self.wallet



  # reduce money in wallet
  def reduce_money(self, amount):
    return self.buy_a_drink(buy)