import time
from archive_functionality import DataBaseNumbers
from checker import Checker
from image_recognition_rollete import ImageRecognition
import datetime
from speak_functionality import VoiceD
import os
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
target_destiantion='/home/danailparvanov/Desktop/Casino/test'
source_destination='/home/danailparvanov/Pictures'

while True:
    cur_time=time.time()
    if cur_time-start_time>=interval:
        t = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        ########### make screenshot
        # del all in target
        del_t = f"rm {target_destiantion}/screen.png"
        os.system(del_t)
        # make screenshot
        scr_make = 'gnome-screenshot'
        os.system(scr_make)
        # move and rename to my folder
        move_ = f"mv {source_destination}/*.png {target_destiantion}/screen.png"
        os.system(move_)

        # ############take source_file
        source_file=f'{target_destiantion}/screen.png'
        # data from reader
        result=ir.main_function(source_file)
        # check for win
        check.prove_if_got_matching(result)
        # store into database
        db.store_new_info(result,t)
        start_time=cur_time








