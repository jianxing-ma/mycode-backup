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

    # deal player2 cards
    hand_player2 = []
    for i in range(2):
        hand_player2.append(deal(deck))

    # deal community cards
    community_cards = []
    for i in range(5):
        community_cards.append(deal(deck))
    print(f"\nCommunity cards are: {show_hand(community_cards)}\n")

    hand_player1 += community_cards
    hand_player2 += community_cards

    ### Check player1's hand-level

    dict_suit = {}
    dict_repeated = {}

    for card in hand_player1:
        dict_suit[card[0]] = dict_suit.get(card[0], 0) + 1
        dict_repeated[card[1]] = dict_repeated.get(card[1], 0) + 1
    
    hand_player1_sorted = sorted(list(dict_repeated.keys()))
    hand_player1_is_straight = False
    if len(hand_player1_sorted) >= 5:
        for i in range(len(hand_player1_sorted) - 4):
            if hand_player1_sorted[i + 4] - hand_player1_sorted[i] == 4:
                hand_player1_is_straight = True
        

    if 4 in dict_repeated.values():
        hand_level_player1 = 7
    elif 3 in dict_repeated.values() and 2 in dict_repeated.values():
        hand_level_player1 = 6
    elif 5 in dict_suit.values() and 6 in dict_suit.values() and \
            7 in dict_suit.values():
        hand_level_player1 = 5
    elif hand_player1_is_straight == True:
        hand_level_player1 = 4
    elif 3 in dict_repeated.values():
        hand_level_player1 = 3
    elif len(dict_repeated) <= 5:
        hand_level_player1 = 2
    elif len(dict_repeated) <= 6:
        hand_level_player1 = 1
    else:
        hand_level_player1 = 0

    print(f"\nPlayer 1's hand is: {HANDLEVEL[hand_level_player1]}\n")


# deal card function
def deal(deck):
    return deck.pop(random.randrange(len(deck)))

def show_hand(hand):
    hand_shown = ""
    for card in hand:
        hand_shown += CARDFIGURE[card[1]] + card[0] + " "
    return hand_shown

if __name__ == "__main__":
    main()
