import datetime

import constants
from utilities.print_with_color import *
from utilities.csv_read_list import *
from utilities.get_current_id import *
from utilities.csv_write import *
from utilities.find_my_cards import *


def sell() :
   cards = find_my_cards()
   cards.pop(0)

   # Check if the user has any cards to sell
   if cards :
      chances = 3
      card_id = ""

      while chances > 0 and not card_id :
         card_id = int(input("\nEnter your id : "))

         card = list(filter(lambda card: int(card[0]) == card_id, cards))

         # Checks if the entered card ID is found in the system
         if not card :
            print_warning("\nCard Not Found!!")

            card_id = ""
            chances -= 1

            if chances == 0 :
               print_error("\nYour chance is over!!")
         else :
            # Checks if the entered card ID already exists in the market data
            cards_market = csv_read_list(constants.CARD_MARKET_CSV)
            cards_market.pop(0)
            is_exist = True if list(filter(lambda card: int(card[1]) == card_id, cards_market)) else False

            if is_exist :
               print_warning("The card already exists in the market")
               
               card_id = ""
               chances -= 1
            else :
               price = int(input("Enter your card price : "))
               
               confirm = input("Are you sure? (y/n) ").lower()

               if confirm == "y" :
                  now = datetime.datetime.now() 
                  formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
                  id = get_current_id(constants.CARD_MARKET_CSV)
                  sell = [
                     id,
                     card_id,
                     price,
                     formatted_date
                  ]

                  method_write = "row"
                  file_handling = "a"

                  if id == 1 :
                     sell = [
                        ["id","card_user_id","price","created_at"],
                        sell
                     ]
                     method_write = "rows"
                     file_handling = "w"
                  
                  csv_write(sell, constants.CARD_MARKET_CSV, method_write, file_handling)

                  print_success("The card was successfully uploaded to the card market")
   else :
      print_warning("\nYou don't have any cards to sell.")

   return



