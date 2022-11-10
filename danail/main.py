import time

from archive_functionality import DataBaseNumbers
from checker import Checker
from read_data_winbet import read_from_win_365
import datetime
check=Checker()
db=DataBaseNumbers()


# run this every 20 sec
start_time=time.time()
interval=2
test=1
while True:
    cur_time=time.time()
    if cur_time-start_time>=interval:
        t = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        if test >10:
            break
        result=read_from_win_365(test-1)
        check.prove_if_got_matching(result)
        db.store_new_info(result,t)
        start_time=cur_time
        test+=1
