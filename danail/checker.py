

class Checker:
    def __init__(self):
        pass

    def check_helper(self,vals):
        pass

    def prove_if_got_matching(self,values:dict):
        for rol_name,val in values.items():
            if self.check_helper(val):
                print('got')

