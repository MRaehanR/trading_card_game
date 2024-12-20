import constants
from utilities.csv_read_list import *
from datetime import datetime, timedelta

def can_user_claim():
    data = csv_read_list(constants.USER_CSV)
    datetime_now = datetime.strptime(datetime.now().strftime(constants.FORMAT_DATE),constants.FORMAT_DATE)
    
    user_last_claim = ""
    for i in range(len(data)):
        if data[i][0] == str(constants.USER_ID) and data[i][4] != "":
            user_last_claim = datetime.strptime(data[i][4], constants.FORMAT_DATE)
            break
        
    if user_last_claim == "" or datetime_now-user_last_claim > timedelta(minutes=constants.CLAIM_TIME_MINUTES):
        return True
    else:
        return False