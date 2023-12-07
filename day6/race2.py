#!/usr/bin/env python3
import sys

def get_win_conditions_count(time, distance):
    total = 0
    for t in range(time):
        remaining_time = time - t
        d = remaining_time * t
        if d > distance:
            total += 1
    return total

def main():
    with open(sys.argv[1], "r") as f:
        records = f.readlines()
    time = int(records[0][records[0].find(":")+1:].strip().replace(" ", ""))
    distance = int(records[1][records[1].find(":")+1:].strip().replace(" ", ""))
    print(get_win_conditions_count(time, distance))

if __name__ == "__main__":
    main()