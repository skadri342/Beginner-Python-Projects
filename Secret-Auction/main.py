import os
from art import logo

auction_dictionary = {}
auction_end = False

def auction_winner():
    highest_bidder = ""
    highest_bid = 0
    for key in auction_dictionary:
        if auction_dictionary[key] >= highest_bid:
            highest_bid = auction_dictionary[key]
            highest_bidder = key
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

def add_to_auction(name, bid_amount):
    auction_dictionary[name] = bid_amount

print(logo)
print("Welcome to the secret auction program.")
while auction_end == False:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    add_to_auction(name, bid_amount)
    while True:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if other_bidders == "yes":
            auction_end = False
            os.system("cls")
            break
        elif other_bidders == "no":
            auction_end = True
            os.system("cls")
            break
auction_winner()