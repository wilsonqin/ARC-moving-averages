from random import randint, seed

class Stock:
  def __init__(self):
    self.price = 50
    self.current_ma = None
    seed()
  def next_price(self):
    new_price = randint(self.price-1, self.price+1)
    self.price = new_price
    return self.price
  def update_ma(self, ma):
    self.current_ma = ma
  def get_ma(self):
    return self.current_ma
