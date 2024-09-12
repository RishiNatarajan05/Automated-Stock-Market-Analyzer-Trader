import robin_stocks.robinhood as r
from config import *

#Log in
login = r.login(r_user_name,r_pwd)


def get_watchlist_stocks():
    """
    Returns all stocks from all watch lists as a list of strings
    """
    all_watch_lists = set()
    all_stocks = set()

    watchlistInfo = r.get_all_watchlists()
    for watch_list in watchlistInfo['results']:
        list_name = watch_list['display_name']
        all_watch_lists.add(list_name)

    for list_name in all_watch_lists:
        watch_list = r.get_watchlist_by_name(name=list_name)
        for item in watch_list['results']:
            stock = item['symbol']
            all_stocks.add(stock)

    return all_stocks


def add_to_watchlist(stock):
    """
    Takes in a string and adds it to default watch list
    """
    r.post_symbols_to_watchlist(stock)


def traverse_watch_list():
    """
        main method - does all necessary watchlist related functions
    """
    print("----- Get all watch list stocks... -----\n")
    watch_list_stocks = get_watchlist_stocks()
    print("Current Watchlist: " + str(watch_list_stocks) + "\n")

traverse_watch_list()

print("Add <stock> to add stock to watchlist, Del <stock> to delete stock from watchlist, Quit to exit")
while True:
    user_input = input("Enter action: ")
    if user_input.lower() == 'quit':
        break
    if "Add " in user_input:
        add_to_watchlist (user_input.replace("Add ", ""))
        traverse_watch_list()
