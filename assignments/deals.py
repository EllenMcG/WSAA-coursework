# Using the this [API](https://deckofcardsapi.com/) that simulates 
# dealing a deck of cards, write a program that "deals" (prints out) 5 cards.
#  Firstly you need to shuffle

import requests

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
if response.status_code == 200:
    deck = response.json()
    deck_id = deck['deck_id']
    print(f"Deck has being shuffled. Deck ID: {deck_id}")
else:
    print("There was an error shuffling the deck. Please try again.")
    exit()

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
if response.status_code == 200:
    cards = response.json()['cards']
    print("Five dealt cards:")
    #for card in cards:
     #   print(f"{card['value']} of {card['suit']}")
    with open("five_dealt_cards.txt", "w") as file:
        file.write(f"Deck ID: {deck_id}\n")
        file.write("Dealt cards:\n")
        for card in cards:
            card_info = f"{card['value']} of {card['suit']}"
            print(card_info)
            file.write(card_info + "\n")
else:
    print("There was an error drawing the cards. Please try again.")