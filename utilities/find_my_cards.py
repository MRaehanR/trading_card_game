from constants import *
from utilities.csv_read_list import *

def find_my_cards () :
   cards = csv_read_list(CARD_USER_CSV)
   my_cards = list(filter(lambda card: not card[1].isnumeric() or int(card[1]) == USER_ID, cards))

   return my_cards