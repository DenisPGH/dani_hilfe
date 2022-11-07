import numpy as np

class Checker:
    def __init__(self):
        self.MATCHING=0 # what kind of folge was
        self.STATUS=False # if the rolet is good or not
        self.COUNT_OF_SAME_VALUES=8
        self.RANGE_SMALL_NUMBERS=16

    def check_helper(self,vals:list):
        list_values=np.array(vals)
        numbers=np.array(list_values[:,0]).astype(int)
        colors=list_values[:,1]
        col,count = np.unique(colors, return_counts=True)

        if col[0]=='r' and count[0]==self.COUNT_OF_SAME_VALUES: # every are 'RED"
            self.STATUS=True
            self.MATCHING='RED'
            return True
        elif col[0]=='b' and count[0]==self.COUNT_OF_SAME_VALUES: # every are 'RED"
            self.STATUS=True
            self.MATCHING = 'BLACK'
            return True

        elif np.all([ True if int(a) > self.RANGE_SMALL_NUMBERS else False  for a in numbers ]): # every are 'BIG"
            self.STATUS=True
            self.MATCHING = 'BIG' # work with 0
            return True

        elif np.all([ True if int(a) <= self.RANGE_SMALL_NUMBERS else False  for a in numbers ]): # every are 'SMALL"
            self.STATUS=True
            self.MATCHING = 'SMALL' #work with 0
            return True

        elif np.all(numbers%2==0): # every are Even
            self.STATUS = True
            self.MATCHING = 'EVEN' #work with 0
            return True
        elif np.all(numbers%2==1): # every are odd
            self.STATUS = True
            self.MATCHING = 'ODD' # dont work with 0
            return True
        return False


    def prove_if_got_matching(self,values:dict):
        self.STATUS = False
        self.MATCHING='nothing'
        for rol_name,val in values.items():
            if self.check_helper(val):
                print(f'Roulette number {rol_name} has a {self.MATCHING}')
                break
        else:
            print('nothing in this turn')

