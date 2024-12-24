import datetime
import constants

from utilities.csv_read_list import *
from utilities.csv_read_list import *
from utilities.csv_write import *
from utilities.get_current_id import *

def register():
    print("\nRegister")
    data = csv_read_list(constants.USER_CSV)
    username_exists = False
    username = str(input("Enter Username: "))
    
    if len(data) == 0:
        for i in data:
            if username in i:
                print("Username already exists")
                username_exists = True
                return False

    if not username_exists:
        password = str(input("Enter Your Password: "))
        id = get_current_id(constants.USER_CSV)
        now = datetime.datetime.now() 
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

        new_user = [
            id, 
            username,
            password,
            100,
            "",
            formatted_date,
        ]

        csv_write(new_user, constants.USER_CSV, "row", "a")
        
        constants.USER_ID = id
                
        print("Registration Successful")
        return True

        

       

            
