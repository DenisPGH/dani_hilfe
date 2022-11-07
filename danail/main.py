from checker import Checker
from read_data_winbet import read_from_win_365
check=Checker()

# run this every 20 sec
result=read_from_win_365()
check.prove_if_got_matching(result)
