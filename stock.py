from random import randint, seed

class Stock:
  def __init__(self):
    self.price = 50
    # MA X_0 condition.
    # by default current moving average = current price
    self.current_ma = 50
    seed()
  def get_price(self):
    return self.price
  def next_price(self):
    new_price = randint(self.price-1, self.price+1)
    self.price = new_price
    return self.price
  def update_ma(self, ma):
    self.current_ma = ma
  def get_ma(self):
    return self.current_ma
