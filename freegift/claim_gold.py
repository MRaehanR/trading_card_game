import constants
from utilities.print_with_color import *
from utilities.can_user_claim import *
from utilities.csv_read_list import *
from utilities.csv_show_table import *
from utilities.get_current_id import *
from utilities.csv_write import *


def claim_gold():
    if not can_user_claim():
        print_warning("You Have Claimed The Gift")
        return
    
    users = csv_read_list(constants.USER_CSV)
    datenow = datetime.now().strftime(constants.FORMAT_DATE)
    
    # Update Card Spread
    for i, user in enumerate(users):
        if user[0] == str(constants.USER_ID):
            updated_user = user
            index_updated_user = i
            break
        
    # Add Gold
    updated_user[3] = int(updated_user[3]) + constants.CLAIM_GOLD_AMOUNT
    updated_user[4] = datenow
    
    # Update User in User_CSV by id
    users[index_updated_user] = updated_user
    
    csv_write(users,constants.USER_CSV,"rows","w")
    
    print_success(f"Congrats! You Got {constants.CLAIM_GOLD_AMOUNT} Gold")