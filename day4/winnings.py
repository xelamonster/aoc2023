#!/usr/bin/env python3
import sys
import math

def get_card_value(card):
    start = card.find(":") + 1
    separator = card.find("|")
    winning_numbers = [int(n) for n in card[start:separator].strip().split()]
    card_numbers = [int(n) for n in card[separator+1:].strip().split()]
    matches = [n for n in card_numbers if n in winning_numbers]
    if len(matches) == 0:
        return 0
    return int(math.pow(2, len(matches) - 1))

def main():
    with open(sys.argv[1], "r") as f:
        cards = f.readlines()
    points = [get_card_value(c) for c in cards]
    print(sum(points))

if __name__ == "__main__":
    main()