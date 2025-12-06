import timeit
from dataclasses import dataclass

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


class Hand:
    card_strength = "23456789TJQKA"

    def __init__(self, card_string, bid):
        self.bid = bid
        self.card_string = card_string
        self.card_values = tuple([self.card_strength.index(card) for card in card_string])        
        self.type = self.get_type()

    def get_type(self):
        card_counts = [self.card_string.count(card) for card in self.card_strength if self.card_string.count(card) > 0]
        card_counts.sort(reverse =  True)
        if card_counts[0] == 5:
            return FIVE_OF_A_KIND
        if card_counts[0] == 4:
            return FOUR_OF_A_KIND
        if card_counts[0] == 3 and card_counts[1] == 2:
            return FULL_HOUSE
        if card_counts[0] == 3:
            return THREE_OF_A_KIND
        if card_counts[0] == 2 and card_counts[1] == 2:
            return TWO_PAIR
        if card_counts[0] == 2:
            return ONE_PAIR
        return HIGH_CARD

    def __lt__(self, other):
        # check if types are different
        if self.type < other.type:
            return True
        if self.type > other.type:
            return False
        # lexicographical ordering of card values as tie breaker
        return self.card_values < other.card_values

    def __repr__(self):
        return f"{self.card_string}"
    

class JokerHand:
    card_strength = "J23456789TQKA"

    def __init__(self, card_string, bid):
        self.bid = bid
        self.card_string = card_string
        self.card_values = tuple([self.card_strength.index(card) for card in card_string])        
        self.type = self.get_type()

    def get_type(self):
        
        card_counts = [self.card_string.count(card) for card in self.card_strength[1:] if self.card_string.count(card) > 0]
        card_counts.sort(reverse =  True)
        # only found jokers
        if len(card_counts) == 0:
            card_counts.append(0)
        card_counts[0] += self.card_string.count("J")
        if card_counts[0] == 5:
            return FIVE_OF_A_KIND
        if card_counts[0] == 4:
            return FOUR_OF_A_KIND
        if card_counts[0] == 3 and card_counts[1] == 2:
            return FULL_HOUSE
        if card_counts[0] == 3:
            return THREE_OF_A_KIND
        if card_counts[0] == 2 and card_counts[1] == 2:
            return TWO_PAIR
        if card_counts[0] == 2:
            return ONE_PAIR
        return HIGH_CARD

    def __lt__(self, other):
        # check if types are different
        if self.type < other.type:
            return True
        if self.type > other.type:
            return False
        # lexicographical ordering of card values as tie breaker
        return self.card_values < other.card_values

    def __repr__(self):
        return f"{self.card_string}"
    

def p1(lines):
    values = 0
    
    hands = []
    for line in lines:
        hands.append(Hand(line.split()[0],int(line.split()[1])))
    hands.sort()

    for i, hand in enumerate(hands):
        #print(f"{hand} Type = {hand.type} Bid = {hand.bid} Rank = {i+1}")
        values += (i+1) * hand.bid
    
    return values


def p2(lines):
    values = 0
    hands = []
    for line in lines:
        hands.append(JokerHand(line.split()[0],int(line.split()[1])))
    hands.sort()

    for i, hand in enumerate(hands):
        #print(f"{hand} Type = {hand.type} Bid = {hand.bid} Rank = {i+1}")
        values += (i+1) * hand.bid
    return values
    

f = open("input7.txt", "r")
lines = [line.strip() for line in f]
#lines = lines[30:100]
  
start = timeit.default_timer()
print (f"Part 1: {p1(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')

start = timeit.default_timer()
print (f"Part 2: {p2(lines)}")
stop = timeit.default_timer()
print(f'Time: {(stop - start):.4}')