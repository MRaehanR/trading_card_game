import constants
import random
from utilities.print_with_color import *
from utilities.can_user_claim import *
from utilities.csv_read_list import *
from utilities.csv_show_table import *
from utilities.get_current_id import *
from utilities.csv_write import *


def reedem_card():
    if not can_user_claim():
        print_warning("You Have Claimed The Gift")
        return
    
    cards = csv_read_list(constants.CARDS_CSV)
    cards_filtered_max_spread = list(filter(lambda card: not (card[2] == card[3]), cards))
    if not len(cards_filtered_max_spread) > 1:
        print_error("There is no left card, please wait admin to add new card!")
        return
    
    # Get All Card_ID
    card_ids = []
    for i in range(1, len(cards_filtered_max_spread)):
        card_ids.append(cards_filtered_max_spread[i][0])
    
    random_card_id = card_ids[random.randint(0,len(card_ids)-1)]
    
    # Create Data card_users
    card_user_star = random.randint(1,5)
    card_user_id = get_current_id(constants.CARD_USER_CSV)
    datenow = datetime.now().strftime(constants.FORMAT_DATE)
    new_card_user = [card_user_id,constants.USER_ID,random_card_id, card_user_star, datenow, datenow]
    
    csv_write(new_card_user, constants.CARD_USER_CSV)
    
    # Update Card Spread
    for i, card in enumerate(cards):
        if card[0] == random_card_id:
            updated_card = card
            index_updated_card = i
            break
    # Add Current Spread
    updated_card[2] = int(updated_card[2]) + 1
    
    # Update Card in Cards_CSV by id
    cards[index_updated_card] = updated_card
    
    csv_write(cards,constants.CARDS_CSV,"rows","w")
    
    
    # Update Last Claim User
    users = csv_read_list(constants.USER_CSV)
    datenow = datetime.now().strftime(constants.FORMAT_DATE)
    
    # Update Card Spread
    for i, user in enumerate(users):
        if user[0] == str(constants.USER_ID):
            updated_user = user
            index_updated_user = i
            break
        
    # Add Gold
    updated_user[4] = datenow
    
    # Update User in User_CSV by id
    users[index_updated_user] = updated_user
    
    csv_write(users,constants.USER_CSV,"rows","w")
    
    print_success("Congrats! You Got New Card")
    return 