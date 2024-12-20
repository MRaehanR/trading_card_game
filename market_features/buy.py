import datetime

import constants
from utilities.print_with_color import *
from utilities.csv_show_table import *
from utilities.csv_read_list import *
from utilities.get_current_id import *
from utilities.csv_write import *
from utilities.find_my_cards import *

def buy() :
   cards_for_sale = csv_read_list(constants.CARD_MARKET_CSV)
   accounts = csv_read_list(constants.USER_CSV)

   # Get User Information
   my_account = list(filter(lambda account: int(account[0]) == int(constants.USER_ID), enumerate(accounts)))[0]

   # Get All My Crads id
   my_cards_id = find_my_cards()
   my_cards_id.pop(0)
   my_cards_id = list(map(lambda card: card[0], my_cards_id))

   # Filter cards available for purchase by the user
   buy_able_crads = cards_for_sale.copy()
   buy_able_crads.pop(0)
   buy_able_crads = list(filter(lambda card: card[1] not in my_cards_id and int(card[2]) <= int(my_account[1][3]), buy_able_crads))

   chances = 3 
   sell_id = ""

   while chances > 0 and not sell_id :
      sell_id = int(input("Enter sell id : "))

      card = list(filter(lambda card: int(card[0]) == sell_id, buy_able_crads))

      if not card :
         print_warning("\nCard Not Found!!")

         sell_id = ""
         chances -= 1

         if chances == 0 :
            print_error("\nYour chance is over!!")
      else :
         card = card[0]
         confirm = input("Are you sure you want to buy this card? (y/n) ").lower()


         if confirm == "y" :
            now = datetime.datetime.now() 
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
         
            # Get Purchased Card Informations
            all_user_cards = csv_read_list(constants.CARD_USER_CSV)
            purchased_card_info = list(filter(lambda purchased: purchased[1][0].isnumeric() and int(purchased[1][0]) == int(card[1]), enumerate(all_user_cards)))[0]

            # # Update Seller Account
            seller_account = list(filter(lambda account: account[1][0].isnumeric() and int(account[1][0]) == int(purchased_card_info[1][1]), enumerate(accounts)))[0]
            
            seller_balance = int(seller_account[1][3]) + int(card[2])
            seller_account[1][3] = seller_balance
            seller_account[1][5] = formatted_date

            accounts[seller_account[0]] = seller_account[1]

            # Update Buyer Account 
            my_balance = int(my_account[1][3]) - int(card[2])
            my_account[1][3] = my_balance
            my_account[1][5] = formatted_date

            accounts[my_account[0]] = my_account[1]

            # Update Card Ownership 
            purchased_card_info[1][1] = constants.USER_ID
            all_user_cards[purchased_card_info[0]] = purchased_card_info[1]

            # Delete Sales Data
            card = list(filter(lambda card: card[1][0].isnumeric() and int(card[1][0]) == sell_id, enumerate(cards_for_sale)))[0]
            cards_for_sale.pop(card[0])


            # Update Data on the Table
            data_to_be_updated = [
               [accounts, constants.USER_CSV],
               [all_user_cards, constants.CARD_USER_CSV],
               [cards_for_sale, constants.CARD_MARKET_CSV]
            ]

            for data in data_to_be_updated :
               csv_write(data[0], data[1], "rows", "w")

            print_success("\nCard successfully purchased")

   return