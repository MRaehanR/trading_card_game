from constants import *
from utilities.csv_read_list import *
from utilities.csv_show_table import *

def profil():
    users = csv_read_list(USER_CSV)
    cards = csv_read_list(CARDS_CSV)

    for i in range(len(users)):
        if users[i][0] == str(USER_ID):
            user_data = users[i]

    card_users = csv_read_list(CARD_USER_CSV)
    card_users_filtered = [card_users[0]]

    # Ubah Bintang
    for i in range(len(card_users)):
        if card_users[i][1] == str(USER_ID):
            card_users[i][3] = int(card_users[i][3])*"⭐"
            card_users_filtered.append(card_users[i])

    # Ubah Nama Kartu
    for i in range(len(card_users_filtered)):
        for j in range(len(cards)):
            if card_users_filtered[i][2] == cards[j][0]:
                card_users_filtered[i][2] = cards[j][1]

    for i in range(len(card_users_filtered)):
        card_users_filtered[i].pop(0)
        card_users_filtered[i].pop(0)

    print("Username: ", user_data[1])
    print(f"Credits: {user_data[3]}🪙")
    print(f"My Cards: {len(card_users_filtered)-1}🃏")

    # Change Header
    card_users_filtered[0] = ["card_name", "stars", "created_at", "updated_at"]
    
    csv_show_table_tabulate(card_users_filtered)

    menu_profile()

def menu_profile():
    print_menu("Profile", ["Back", "Logout"])
    chosenMenu = int(input("Option: "))

    if chosenMenu == 1:
        print("MainMenu")
    elif chosenMenu == 0:
        print("See You Later!")
        exit() 
    else:
        print_error("Choose the correct number!")

def print_menu(title, options) :
    print(f"\n\n{title}")
    for key, option in enumerate(options, 1) :

        if key == len (options): key = 0
        print(f"[{key}] {option}")