import time
from archive_functionality import DataBaseNumbers
from checker import Checker
from image_recognition_rollete import ImageRecognition
from read_data_winbet import read_from_win_365
import datetime
check=Checker()
db=DataBaseNumbers()
ir=ImageRecognition()


# run this every 20 sec
start_time=time.time()
interval=2
test=1
while True:
    cur_time=time.time()
    if cur_time-start_time>=interval:
        t = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        if test >2:
            break
        # make screenshot

        # source_file
        source_file='screen_/scr_1.png'
        # data from reader
        result=ir.main_function(source_file)
        # check for win
        check.prove_if_got_matching(result)
        # store into database
        db.store_new_info(result,t)
        start_time=cur_time
        test+=1
