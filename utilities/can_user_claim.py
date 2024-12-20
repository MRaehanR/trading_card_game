import constants
from utilities.csv_read_list import *
from datetime import datetime, timedelta

def can_user_claim():
    data = csv_read_list(constants.USER_CSV)
    datetime_now = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
    
    for i in range(len(data)):
        if data[i][0] == str(constants.USER_ID):
            user_last_claim = datetime.strptime(data[i][4], "%Y-%m-%d %H:%M:%S")
            break
        
    if datetime_now-user_last_claim > timedelta(minutes=constants.CLAIM_TIME_MINUTES):
        return True
    else:
        return False