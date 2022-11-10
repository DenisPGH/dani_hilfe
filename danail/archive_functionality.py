import csv
import time
import datetime
class DataBaseNumbers:
    def __init__(self):
        self.time_=datetime.datetime.today()
    def store_new_info(self,dict_):
        """
        store the every new line into db
        :param dict_: dict_={ number_rollete:[(number,color),(number,color)],...}
        :return:
        """

        for name,values in dict_.items():
            last_value=values[-1][0]
            last_value_color=values[-1][1]
            with open(f'roulette{name}.csv', mode='a', newline='') as csv_write:  # w,a
                file = csv.writer(csv_write, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file.writerow([self.time_,name,last_value,last_value_color])

    def return_info_db(self,number_rollete):
        # read
        with open(f'roulette{number_rollete}.csv', mode='r', newline='') as csv_read:  # w,a
            print(csv_read.readlines())





