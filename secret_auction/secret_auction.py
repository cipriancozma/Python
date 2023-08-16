from logo import logo

print(logo)

name_input = input("What is your name?:")
bid_price = int(input("What's your bid?:"))
auction_dictionary = {}
auction_dictionary[name_input] = bid_price

question = input("Are there any other bidders? Type 'yes' or 'no'.")

while question == 'yes':
    name_input = input("What is your name?:")
    bid_price = int(input("What's your bid?:"))
    auction_dictionary[name_input] = bid_price
    question = input("Are there any other bidders? Type 'yes' or 'no'.")

if question == 'no':
    max_key = max(auction_dictionary, key=auction_dictionary.get)
    max_value = max(auction_dictionary.values())

    print(f"The winner is {max_key} with a bid of ${max_value}")