# Using the this [API](https://deckofcardsapi.com/) that simulates 
# dealing a deck of cards, write a program that "deals" (prints out) 5 cards.
#  Firstly you need to shuffle
# This script will shuffle a deck of cards, draw 5 cards, and check for special combinations
# like pairs, triples, straights, and flushes.
# Using the this [API](https://deckofcardsapi.com/) 

import requests

def check_hand(cards):
    '''
    Check the hand for special combinations like pairs, triples, straights, and flushes.
    Parameters:
        cards (list): A list of dictionaries representing the dealt cards.
    Returns:
        None
    '''

    values = [card['value'] for card in cards]
    suits = [card['suit'] for card in cards]

    # Convert face cards to numerical values for easier comparison
    value_map = {
        "ACE": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
        "9": 9, "10": 10, "JACK": 11, "QUEEN": 12, "KING": 13
    }
    numeric_values = sorted([value_map[value] for value in values])

    # Check for pairs, triples, and straights
    value_counts = {value: values.count(value) for value in values}
    if 3 in value_counts.values():
        print("Congratulations! You have a triple!")
    elif 2 in value_counts.values():
        print("Congratulations! You have a pair!")

    # Check for a straight (5 consecutive values)
    if len(numeric_values) == 5 and numeric_values[-1] - numeric_values[0] == 4 and len(set(numeric_values)) == 5:
        print("Congratulations! You have a straight!")

    # Check for all cards of the same suit
    if len(set(suits)) == 1:
        print("Congratulations! All cards are of the same suit!")

shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
if response.status_code == 200:
    deck = response.json()
    deck_id = deck['deck_id']
    print(f"Deck has been shuffled. Deck ID: {deck_id}")
else:
    print("There was an error shuffling the deck. Please try again.")
    exit()

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
if response.status_code == 200:
    cards = response.json()['cards']
    print("Five dealt cards:")
    with open("dealt_cards.txt", "w") as file:
        file.write(f"Deck ID: {deck_id}\n")
        file.write("Dealt cards:\n")
        for card in cards:
            card_info = f"{card['value']} of {card['suit']}"
            print(card_info)
            file.write(card_info + "\n")

    check_hand(cards)
else:
    print("There was an error drawing the cards. Please try again.")