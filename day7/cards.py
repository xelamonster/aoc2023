#!/usr/bin/env python3
import sys
import functools

deck = "23456789TJQKA"

def score_hand(hand):
    card_counts = [(hand.count(c), c) for c in deck]
    card_counts.sort(key=lambda x: x[0], reverse=True)
    if card_counts[0][0] == 5:  # five of a kind
        return 6
    if card_counts[0][0] == 4:  # four of a kind
        return 5
    if card_counts[0][0] == 3:
        if card_counts[1][0] == 2:  # full house
            return 4
        return 3  # three of a kind
    if card_counts[0][0] == 2:
        if card_counts[1][0] == 2:  # two pair
            return 2
        return 1  # one pair
    return 0  # high card

def compare_hand(a, b):
    if a[2] != b[2]:
        return a[2] - b[2]
    i = 0
    while a[0][i] == b[0][i]:
        i += 1
    return deck.find(a[0][i]) - deck.find(b[0][i])

def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
    hands = [l.strip().split() for l in data]
    scored_hands = [(h[0], int(h[1]), score_hand(h[0])) for h in hands]
    scored_hands.sort(key=functools.cmp_to_key(compare_hand))
    winnings = [(i+1) * int(h[1]) for i, h in enumerate(scored_hands)]
    print(sum(winnings))

if __name__ == "__main__":
    main()