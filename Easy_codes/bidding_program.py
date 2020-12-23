from replit import clear
# HINT: You can call clear() to clear the output in the console.
from Easy_codes.art import logo1

print(logo1)

bidding_people = {}


# function to add the bidder
def add_bidder(bidder, amount):
    bidding_people[bidder] = amount


# function to get the highest bidder
def highest_bidder():
    max_bid = 0
    max_bidder_name = ''
    for name in bidding_people:
        amount = int(bidding_people[name])
        if max_bid < amount:
            max_bidder_name = name
            max_bid = bidding_people[name]
    print(f"Congratulation! {max_bidder_name} has won the auction with {max_bid}")


end_bidding = False
while not end_bidding:
    bidder_name = input("Enter the Name: ")
    bid_amount = int(input("Enter the bidding amount: $"))
    add_bidder(bidder_name, bid_amount)
    user_input = input("Enter 'yes' if there are other people else 'no': ")
    if user_input == "yes":
        clear()
        # print(bidding_people)
    else:
        end_bidding = True
        highest_bidder()



