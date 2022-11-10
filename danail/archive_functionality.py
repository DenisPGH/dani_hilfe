import csv
import time
import datetime
class DataBaseNumbers:
    def __init__(self):
        self.time_= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.LAST_DICT_VALUES ={1:[],2:[],3:[]}
        self.path_store_rolete_info='db_store'
        self.how_many_values_to_compare=4
    def store_new_info(self,dict_,time_):
        """
        store the every new line into db, if it a new number came
        :param time_: current time
        :param dict_: dict_={ number_rollete:[(number,color),(number,color)],...}
        :return:
        """
        for name,values in dict_.items():
            if self.LAST_DICT_VALUES[name][-self.how_many_values_to_compare:]==\
                    dict_[name][-self.how_many_values_to_compare:]: # last four values
                continue
            last_value=values[-1][0]
            last_value_color=values[-1][1]
            with open(f'{self.path_store_rolete_info}/roulette{name}.csv', mode='a', newline='') as csv_write:  # w,a
                file = csv.writer(csv_write, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file.writerow([time_,name,last_value,last_value_color])
        self.LAST_DICT_VALUES = dict_

    def return_info_db(self,number_rollete):
        # read
        with open(f'{self.path_store_rolete_info}/roulette{number_rollete}.csv', mode='r', newline='') as csv_read:  # w,a
            print(csv_read.readlines())






