import time

from checker import Checker
from read_data_winbet import read_from_win_365
check=Checker()

# run this every 20 sec
start_time=time.time()
interval=20
while True:
    cur_time=time.time()
    if cur_time-start_time>=interval:
        result=read_from_win_365()
        check.prove_if_got_matching(result)
        start_time=cur_time
