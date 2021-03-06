from stock import Stock
from Queue import Queue
from arc_utils import print_ma

#M, the number of days we care about
ma_days = 10

#simulation length in days
sim_len = 50

#initialize the first ma_days of data
def populate_mem(memory, s):
  m_sum = 0
  while not memory.full():
    next_price = s.next_price()
    memory.put(next_price)
    m_sum += next_price
  ma_current = float(m_sum) / float(ma_days)
  s.update_ma(ma_current)

# calculate the next moving average
# hint: do we know the current moving avg?
def populate_ma(ma_arr, memory, s):
  # >>>>>> TODO
  return

def main():
  s = Stock()

  # this is the data structure we use to store our data points (stock prices)
  # we will need to access them later in our second pass 
  memory = Queue(maxsize=ma_days)

  #we want to build a sequential list of the moving avgs as we calculate them
  #this is what ma_arr is for storing
  ma_arr = []

  populate_mem(memory, s)
  
  #hint: remember to populate the moving avg array with the first one.
  #     you can do it here, or make some modifications to the populate_mem step

  #Here you will run your simulation 
  for x in range(1,sim_len,1):
    populate_ma(ma_arr, memory, s)

  #pretty prints our array of moving avgs  
  map(print_ma, ma_arr)

main()