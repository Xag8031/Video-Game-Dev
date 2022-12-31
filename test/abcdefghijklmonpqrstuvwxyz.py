import builtins; builtins.os
import sys


print(1)
#close the program and open a different file.

# stop the current program and start the run.py program
os.exec('python run.py')
# this code will not be reached
sys.exit(0)