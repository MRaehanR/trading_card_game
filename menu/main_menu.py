from utilities.csv_show_table import *
from utilities.find_my_cards import *
from utilities.csv_read_list import *
from market_features.sell import *
from market_features.cancel import *
from market_features.buy import *
from authentications.register import *
from authentications.login import *
from profile.profil import *
from freegift.redeem_card import *
from freegift.claim_gold import *

def print_menu(title, options) :
    print(f"\n\n{title}")
    for key, option in enumerate(options, 1) :

        if key == len (options): key = 0
        print(f"[{key}] {option}")


def login_and_register():
    print_menu("Welcome To Terminal TCG",["Login", "Register", "Exit"])
    chosenMenu = int(input("Option: "))
    
    if chosenMenu == 1:
        login()
    elif chosenMenu == 2:
        register()
    elif chosenMenu == 0:
        print("See You Later!")
        exit()
    else:
         print_error("Choose the correct number!")
         
    main_menu()

def main_menu():
    print_menu("Main Menu", ["Sell Card", "Buy Card", "Profile", "Free Gift", "Logout"])
    chosenMenu = int(input("Option: "))
    print("\n")

    if chosenMenu == 1:
        sell_card()
    elif chosenMenu == 2:
        buy_card()
    elif chosenMenu == 3:
        profile()
    elif chosenMenu == 4:
        free_gift()
    elif chosenMenu == 0:
        print("See You Later!")
        exit() 

    else:
        print_error("Choose the correct number!")

def sell_card():
    print_menu("Sell Card", ["Sell Card", "Cancel Sell Card", "Back"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        print("\n\nMarket")
        market_card = csv_read_list(constants.CARD_MARKET_CSV)
        csv_show_table_tabulate(market_card)
        
        print("\n\nMy Card")
        show_my_cards()
        
        sell()
    elif chosenMenu == 2:
        show_my_cards()
        cancel()
    elif chosenMenu == 0:
        main_menu()
    else: 
        print_error("Choose the correct number!")
    main_menu()

def show_my_cards():
    cards = csv_read_list(constants.CARDS_CSV)
    my_cards = find_my_cards()
        
    # Ubah Bintang
    for i in range(len(my_cards)):
        if my_cards[i][1] == str(constants.USER_ID):
            my_cards[i][3] = int(my_cards[i][3])*"⭐"

    # Ubah Nama Kartu
    for i in range(len(my_cards)):
        for j in range(len(cards)):
            if my_cards[i][2] == cards[j][0]:
                my_cards[i][2] = cards[j][1]
    for i in range(len(my_cards)):
        my_cards[i].pop(1)
    csv_show_table_tabulate(my_cards)

def buy_card():
    print_menu("Buy Card", ["Buy Card", "Back"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        print ("\n\nMarket")
        csv_show_table_tabulate(constants.CARD_MARKET_CSV)
        print("\n\nMy Card")
        my_card = find_my_cards()
        csv_show_table_tabulate(my_card)
        buy()
    elif chosenMenu == 0:
        main_menu()
    else:
       print_error("Choose the correct number!") 
       
    main_menu()


def profile():
    profil()
    print_menu("Profile", ["Back", "Logout"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        main_menu()
    elif chosenMenu == 0:
        print("See You Later!")
        exit() 
    else:
        print_error("Choose the correct number!")
        

def free_gift():
    print_menu("Free Gift", ["Redeem Card", "Redeem Gold"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        reedem_card()
    elif chosenMenu == 0:
        claim_gold()
    else:
        print_error("Choose the correct number!") 
        
    main_menu()


        
