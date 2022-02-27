""" Silent Auction v1 - to run a silent auction
Created by Joseph Wong
25/02/2022
"""


# Auctioning Function
def auction_cycle():
    global enter_bid
    global highest_bid
    while enter_bid != -1:
        enter_bid = float(input("What is your bid? "))
        if highest_bid > enter_bid:
            print("Please enter a higher bid")
            print(f"Highest bid so far is ${highest_bid}")
        else:
            print(f"Highest bid so far is ${enter_bid}")
            highest_bid = enter_bid


# Main Routine
item = input("What is the auction for? ")
reserve_price = int(input("What is the reserve price? "))
print()
print(f"The auction for the {item} has started!")
print()
start_bid = 0
print(f"Highest bid so far is ${start_bid}")
enter_bid = 0
highest_bid = 0
auction_cycle()
print()
if highest_bid >= reserve_price:
    print(f"The auction for the {item} finished with a bid of ${highest_bid}")
else:
    print(f"The {item} didn't sell!")
