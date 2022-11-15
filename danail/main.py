import time
from archive_functionality import DataBaseNumbers
from checker import Checker
from image_recognition_rollete import ImageRecognition
import datetime
from speak_functionality import VoiceD
check=Checker()
db=DataBaseNumbers()
ir=ImageRecognition()
stimme=VoiceD()

st="Start the program for searching!"
stimme.speak_this(st)
print(st)
# run this every 20 sec
start_time=time.time()
interval=2

while True:
    cur_time=time.time()
    if cur_time-start_time>=interval:
        t = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
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

