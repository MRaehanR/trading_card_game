from utilities.csv_show_table import *
from market_features.sell import *
from market_features.cancel import *
from market_features.buy import *
from utilities.find_my_cards import *
from utilities.csv_read_list import *

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

def main_menu():
    print_menu("Main Menu", ["Sell Card", "Buy Card", "Porfile", "Free Gift", "Logout"])
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
        market_card = csv_read_list(CARD_MARKET_CSV)
        market_card = list(map(lambda card: , market_card))
        print("\n\nMy Card")
        my_card = find_my_cards()
        csv_show_table_tabulate(my_card)
        data_sell_card = []
        for card in market_card:
            for cards in my_card:
                if card [1] == cards [0]:
                    data_sell_card.append(card)
        print(data_sell_card)
        sell()
    elif chosenMenu == 2:
        cancel()
    elif chosenMenu == 0:
        main_menu()
    else: 
        print_error("Choose the correct number!")


def buy_card():
    print_menu("Buy Card", ["Buy Card", "Back"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        print ("\n\nMarket")
        csv_show_table_tabulate(CARD_MARKET_CSV)
        print("\n\nMy Card")
        my_card = find_my_cards()
        csv_show_table_tabulate(my_card)
        buy()
    elif chosenMenu == 0:
        main_menu()
    else:
       print_error("Choose the correct number!") 


def profile():
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
        redeem_card()
    elif chosenMenu == 2:
        redeem_gold()
    else:
        print_error("Choose the correct number!") 


        
