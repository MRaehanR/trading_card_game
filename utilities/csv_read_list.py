import csv
import os
import constants
from utilities.csv_write import *

def csv_read_list(filepath):
    if os.path.exists(filepath):
        with open(str(filepath), 'r') as File:
            csv_reader = csv.reader(File)
            return list(csv_reader)
    else:
        if filepath == constants.USER_CSV:
            header = ['id','username','password','gold','last_gift_claim','created_at']
        elif filepath == constants.CARDS_CSV:
            header = ['id','name','spread','max_spread','created_at']
        elif filepath == constants.CARD_USER_CSV:
            header = ['id','user_id','card_id','star','created_at','updated_at']
        elif filepath == constants.CARD_MARKET_CSV:
            header = ['id','card_user_id','price','created_at']
            
        csv_write(header, filepath, "row", "w")