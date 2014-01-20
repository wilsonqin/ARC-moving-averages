from stock import Stock
from Queue import Queue

# we can use the recurrence equation to obtain the EMA
# X_{0,a} = D_0
# X_{t,a} = (1-a) * D_t + a * X_{t-1,a}

#M, the number of days we care about
ma_days = 10

# alpha, must satisfy 0 < a <= 1 
alpha = 0.90

#simulation length in days
sim_len = 50

# calculate the next moving average, using the current one
# using our knowledge of the recurrence equation
def populate_ma(ma_arr, s):
  new_price = s.next_price()
  new_ma = ((1 - alpha) * new_price) + (alpha * s.get_ma())
  s.update_ma(new_ma)
  ma_arr.append(new_ma)

def print_ma(ma):
  print ("%.2f" % ma)

def main():
  s = Stock()
  ma_arr = []

  #populate the moving avg array with the first one
  ma_arr.append(s.get_ma())

  #loop that actually runs the simulation
  for x in range(1,sim_len,1):
    populate_ma(ma_arr, s)

  #pretty prints our array of moving avgs
  map(print_ma, ma_arr)

main()