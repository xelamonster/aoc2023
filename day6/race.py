#!/usr/bin/env python3
import sys
import functools

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
    times = [int(n) for n in records[0][records[0].find(":")+1:].strip().split()]
    distances = [int(n) for n in records[1][records[1].find(":")+1:].strip().split()]
    win_conditions_counts = [
        get_win_conditions_count(times[i], distances[i])
        for i in range(len(times))
    ]
    print(functools.reduce(lambda a, b: a * b, win_conditions_counts))

if __name__ == "__main__":
    main()