from stock import Stock
from Queue import Queue
from arc_utils import print_ma

#M, the number of days window used to calc. our moving avg
ma_days = 10

# alpha, must satisfy 0 < a <= 1 
alpha = 0.90

#simulation length in days
sim_len = 50

# calculate the next moving average, using the current one
# using our knowledge of the recurrence equation
def populate_ma(ma_arr, s):
  # >>>>>> TODO
  # you will want to calculate your next moving average
  # and remember to keep it for your records
  return

def main():
  s = Stock()

  #we want to build a sequential list of the moving avgs as we calculate them
  #this is what ma_arr is for storing
  ma_arr = []

  #hint: remember to populate the moving avg array with the first one

  #>>>>>> TODO: Here you will run your simulation
  for x in range(1,sim_len,1):
    populate_ma(ma_arr, s)

  #pretty prints our array of moving avgs
  map(print_ma, ma_arr)

main()