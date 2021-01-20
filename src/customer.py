class Customer:

  def __init__(self, name, wallet):
    self.name = name
    self.wallet = wallet

# remove moeny from wallet
  def remove_money_wallet(self, amount):
    self.wallet -= amount


