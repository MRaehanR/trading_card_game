import os

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
CSV_BASE_PATH=f"{BASE_PATH}/csv"
USER_CSV=f"{CSV_BASE_PATH}/users.csv"
CARD_USER_CSV=f"{CSV_BASE_PATH}/card_users.csv"
CARDS_CSV=f"{CSV_BASE_PATH}/cards.csv"
CARD_MARKET_CSV=f"{CSV_BASE_PATH}/card_market.csv"
CARDS_CSV=f"{CSV_BASE_PATH}/cards.csv"
CLAIM_TIME_MINUTES=5 # in minutes
FORMAT_DATE="%Y-%m-%d %H:%M:%S"
CLAIM_GOLD_AMOUNT=100
USER_ID=None
