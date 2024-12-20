import constants
from utilities.print_with_color import *
from utilities.csv_read_list import *
from utilities.csv_write import *
from utilities.find_my_cards import *


def cancel() :
   cards_for_sale = csv_read_list(constants.CARD_MARKET_CSV)

   my_cards_for_sale = cards_for_sale.copy()
   my_cards_for_sale.pop(0)

   my_cards_id = find_my_cards()
   my_cards_id.pop(0)
   my_cards_id = list(map(lambda card: card[0], my_cards_id))

   my_cards_for_sale = list(filter(lambda card: card[1] in my_cards_id, my_cards_for_sale))

   if my_cards_for_sale :
      card_id = int(input("\nEnter your id : "))

      card = list(filter(lambda card: int(card[0]) == card_id, my_cards_for_sale))

      if card :
         confirm = input("\nAre you sure you want to cancel the sale of this card? (y/n) ").lower()

         if confirm == "y" :
            cards_for_sale = list(filter(lambda card: not card[0].isnumeric or str(card[0]) != str(card_id), cards_for_sale))

            csv_write(cards_for_sale, constants.CARD_MARKET_CSV, "rows", "w")

            print_success("\nSuccessfully canceled the sale.")
      else :
         print_warning("\nCard Not Found!!")

   else :
      print_warning("\nYou do not have any cards listed for sale.")

   return
