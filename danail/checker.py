import numpy as np

from speak_functionality import Voice


class Checker:
    def __init__(self):
        self.MATCHING=0 # what kind of folge was
        self.STATUS=False # if the rolet is good or not
        self.COUNT_OF_SAME_VALUES=8
        self.RANGE_SMALL_NUMBERS=16
        self.stimme=Voice()


    def check_helper(self,vals:list):
        """

        :param vals: list allways with len ==8
        :return: true if macht, false if not
        """
        list_values=np.array(vals)
        numbers=np.array(list_values[:,0]).astype(int)
        colors=list_values[:,1]
        col,count = np.unique(colors, return_counts=True)
        dict_compact=dict(zip(col,count))
        if 'r' not in dict_compact.keys():
            dict_compact['r']=0
        if 'b' not in dict_compact.keys():
            dict_compact['b']=0
        if 'rb' not in dict_compact.keys():
            dict_compact['rb']=0


        if col[0]=='r' and count[0]==self.COUNT_OF_SAME_VALUES or \
            dict_compact['r']==self.COUNT_OF_SAME_VALUES-dict_compact['rb']: # every are 'RED"
            self.STATUS=True
            self.MATCHING='RED' # work with 0
            return True
        elif col[0]=='b' and count[0]==self.COUNT_OF_SAME_VALUES or \
                dict_compact['b']==self.COUNT_OF_SAME_VALUES-dict_compact['rb']: # every are 'RED"
            self.STATUS=True
            self.MATCHING = 'BLACK' # work with 0
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

        # ODD here
        if 0 in numbers:
            numbers[numbers==0]=1
        if np.all(numbers%2==1): # every are odd
            self.STATUS = True
            self.MATCHING = 'ODD' #work with 0
            return True
        return False


    def prove_if_got_matching(self,values:dict):
        """

        :param values: dict {rol_name: list[(number,color)],rol_name_2:....}
        :return: if find match break the for and speak the result, if not just print
        """
        self.STATUS = False
        self.MATCHING='nothing'
        for rol_name,val in values.items():
            if not len(val)== self.COUNT_OF_SAME_VALUES: # if less than wished values jump this rolete
                continue
            if self.check_helper(val):
                text=f'Roulette number {rol_name} has a {self.MATCHING}'
                print(text)
                # speak this uncomment later
                #self.stimme.speak_this(text)
                break
        else:
            print('NO MATCH this turn!!!!')

