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
        if login():
            main_menu()
        else:
            login_and_register()
    elif chosenMenu == 2:
        if register():
            main_menu()
        else:
            login_and_register()
    elif chosenMenu == 0:
        print("See You Later!")
        exit()
    else:
        print_error("Choose the correct number!")
        login_and_register()

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

def detail_market_cards(type) :
    cards_market = csv_read_list(constants.CARD_MARKET_CSV)
    cards        = csv_read_list(constants.CARDS_CSV)
    cards_user   = csv_read_list(constants.CARD_USER_CSV)
    users        = csv_read_list(constants.USER_CSV)

    details = [
        ["sell_id", "card_name", "star", "price", "seller", "created_at"]
    ]

    cards_market.pop(0)
    for market in cards_market :
        card_user_detail = list(filter(lambda card: card[0] == market[1], cards_user))[0]
        seller_detail    = list(filter(lambda user: user[0] == card_user_detail[1], users))[0]
        name    = list(filter(lambda card: card[0] == card_user_detail[2], cards))[0][1]
        star    = int(card_user_detail[3])*"⭐"

        detail = [
            market[0],
            name,
            star,
            market[2],
            seller_detail[1],
            market[3]
        ]

        # Get the details of the card that the user is selling or that the user can buy.
        if (type == "sell" and int(seller_detail[0]) == int(constants.USER_ID)) or (type == "buy" and int(seller_detail[3]) >= int(market[2])) :
            details.append(detail)
    
    csv_show_table_tabulate(details)

def sell_card():
    print("\n\My Cards in Market")
    detail_market_cards("sell")
    
    print("\n\nMy Card")
    show_my_cards()

    print_menu("Sell Card", ["Sell Card", "Cancel Sell Card", "Back"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1: 
        print("\n\nMy Cards")     
        show_my_cards()
        sell()
    elif chosenMenu == 2:
        print("\n\nMy cards that are currently for sale.")
        detail_market_cards("sell")
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
    print("\n\nMarket")
    detail_market_cards("buy")
    
    print("\n\nMy Card")
    show_my_cards()

    print_menu("Buy Card", ["Buy Card", "Back"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
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


        
