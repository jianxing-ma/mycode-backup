#!/user/bin/python3

import random

HANDLEVEL = {0: "high card", 1: "one pair", 2: "two pair", 3: "trips", 4: "straight", 5: "flush", 6: "full house", 7: "quads", 8: "straight flush"}
CARDFIGURE = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K", 14: "A"}

def main():

    # create card deck
    deck = []
    for i in ('♠', '♦', '♥', '♣'):
        for j in range(2, 15):
            deck.append((i, j))
    
    # deal player1 cards
    hand_player1 = []
    for i in range(2):
        hand_player1.append(deal(deck))
    print(f"\nPlayer 1's hole cards: {show_hand(hand_player1)}\n")

    # deal community cards
    community_cards = []
    for i in range(5):
        community_cards.append(deal(deck))
    print(f"\nCommunity cards are: {show_hand(community_cards)}\n")

    hand_player1 += community_cards

    print(f"\nPlayer 1's hand is {HANDLEVEL[get_hand_level(hand_player1)[0]]}: {show_hand(get_hand_level(hand_player1)[1])}")


### Get player1's hand-level
def get_hand_level(hand):
    dict_suit = {}
    dict_repeated = {}

    for card in hand:
        # dict_suit[card[0]] = dict_suit.get(card[0], 0) + 1
        dict_suit[card[0]] = dict_suit.get(card[0], []) + [card]
        dict_suit_sorted = dict(sorted(dict_suit.items(), key = lambda kv: len(kv[1]), reverse=True))
        list_suit_count = [(key, len(dict_suit_sorted[key])) for key in dict_suit_sorted]

        # dict_repeated[card[1]] = dict_repeated.get(card[1], 0) + 1
        dict_repeated[card[1]] = dict_repeated.get(card[1], []) + [card]
        dict_repeated_sorted = dict(sorted(dict_repeated.items(), key = lambda kv: (len(kv[1]), kv[0]), reverse = True))
        list_repeated_count = [(key, len(dict_repeated_sorted[key])) for key in dict_repeated_sorted]
        
    hand_figure_sorted = sorted(list(dict_repeated.keys()))
    hand_is_straight = False
    if len(hand_figure_sorted) >= 5:
        for i in range(len(hand_figure_sorted) - 4):
            if hand_figure_sorted[i + 4] - hand_figure_sorted[i] == 4:
                hand_is_straight = True
        

    if list_repeated_count[0][1] == 4:
        hand_level = 7
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 2)
    elif list_repeated_count[0][1] == 3 and list_repeated_count[1][1] == 2:
        hand_level = 6
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 2)
    elif list_suit_count[0][1] >= 5:
        hand_level = 5
        hand_result = dict_suit_sorted[list_suit_count[0][0]]
    elif hand_is_straight == True:
        hand_level = 4
        hand_result = hand_figure_sorted
    elif list_repeated_count[0][1] == 3:
        hand_level = 3
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 3)
    elif len(list_repeated_count) <= 5:
        hand_level = 2
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 3)
    elif len(list_repeated_count) <= 6:
        hand_level = 1
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 4)
    else:
        hand_level = 0
        hand_result = retrieve_hand_result(dict_repeated_sorted, list_repeated_count, 5)

    return hand_level, hand_result

### helper function to get hand result
def retrieve_hand_result(dict_hand, list_hand, n):
    hand_result = []

    for i in range(n):
        hand_result += dict_hand[list_hand[i][0]]
    return hand_result

### helper function to deal cards
def deal(deck):
    return deck.pop(random.randrange(len(deck)))

### helper function to print cards
def show_hand(hand):
    hand_shown = ""
    for card in hand:
        hand_shown += CARDFIGURE[card[1]] + card[0] + " "
    return hand_shown

if __name__ == "__main__":
    while input("\nEnter Play(P): ").capitalize() == "P":
        main()
