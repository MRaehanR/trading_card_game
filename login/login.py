from utilities.csv_read_list import *
import constants

def login():
    is_login_success = False
    attempts = 1
    
    while not is_login_success and attempts <= 3:
        username = input("Enter username:")
        password = input("Enter password:")

        data = csv_read_list(constants.USER_CSV)

        for i in range (len(data)):
            if username in data[i] and password in data[i]:
                is_login_success = True
                constants.USER_ID = data[i][0]
        
        if not is_login_success:
            print("Login failed, please try again.")

        attempts += 1
    
    if is_login_success:
        print("Login succesfully!")
    else:
        print("Maximum attempts login, access denied.")