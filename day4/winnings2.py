#!/usr/bin/env python3
import sys
import math

def get_card_value(card):
    start = card.find(":") + 1
    separator = card.find("|")
    n = int(card[:start-1].strip().split()[1])
    winning_numbers = [int(n) for n in card[start:separator].strip().split()]
    card_numbers = [int(n) for n in card[separator+1:].strip().split()]
    matches = [n for n in card_numbers if n in winning_numbers]
    if len(matches) == 0:
        return None
    return (n, n + len(matches))

def main():
    with open(sys.argv[1], "r") as f:
        cards = f.readlines()
    total = 0
    end = len(cards)
    card_values = [get_card_value(c) for c in cards]
    new_card_values = card_values
    while True:
        total += len(new_card_values)
        new_card_values = [
            card_values[c[0]:c[1] if c[1] < end else end]
            for c in new_card_values
            if c is not None
        ]
        new_card_values = [c for entry in new_card_values for c in entry] # flatten
        if len(new_card_values) == 0:
            break
    print(total)

if __name__ == "__main__":
    main()