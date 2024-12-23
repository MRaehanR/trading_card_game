import os
from utilities.csv_read_list import *


def get_current_id(filepath) :
   data = csv_read_list(filepath)
   if os.path.exists(filepath) and len(data) > 1:
      current_id = int(data[len(data) - 1][0]) + 1
   else :
      current_id = 1
      
   return current_id