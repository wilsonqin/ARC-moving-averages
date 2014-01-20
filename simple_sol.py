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

def populate_ma(ma_arr, memory, s):
  removed = memory.get()
  assert (memory.qsize() == ma_days-1)
  new_price = s.next_price()
  new_ma = s.get_ma() - (float(removed) / ma_days) + (float(new_price) / ma_days)
  s.update_ma(new_ma)
  memory.put(new_price)
  ma_arr.append(new_ma)

def main():
  s = Stock()
  memory = Queue(maxsize=ma_days)
  ma_arr = []
  populate_mem(memory, s)
  #populate the moving avg array with the first one
  ma_arr.append(s.get_ma())

  for x in range(1,sim_len,1):
    populate_ma(ma_arr, memory, s)
  map(print_ma, ma_arr)

main()