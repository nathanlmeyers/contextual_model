import os
import sys
from ops.db_utils import get_status

#This script just makes it easy to check the status of the db
#without logging into it. If you want to check the progress of
#the run (assuming you are using bayes_opt_all as the table),
#just run:

##### python status.py bayes_opt_all

#from the terminal

tb_name = sys.argv[1]
print "\nThere are " + str(int(get_status(tb_name)[0][0])) + " entries in this table\n"
