from utilities.csv_read_list import *
import constants

def login():
    is_login_success = False
    attempts = 1
    
    while not is_login_success and attempts <= 3:
        username = input("Enter username:")
        password = input("Enter password:")

        users = csv_read_list(constants.USER_CSV)

        for i in range (len(users)):
            if username == users[i][1] and password == users[i][2]:
                is_login_success = True
                constants.USER_ID = users[i][0]
        
        if not is_login_success:
            print("Login failed, please try again.")

        attempts += 1
    
    if is_login_success:
        print("Login succesfully!")
    else:
        print("Maximum attempts login, access denied.")