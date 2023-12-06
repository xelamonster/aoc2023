#!/usr/bin/env python3
import sys

TOTAL_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def parse_game_record(record):
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    start = record.find(":")
    end = record.find(";")
    if end == -1:
        end = len(record)
    id = int(record[0:start].split(" ")[1])
    while start < len(record):
        round = [r.strip().split(" ") for r in record[start+1:end].split(",")]
        for r in round:
            print(r)
            n = int(r[0].strip())
            color = r[1].strip()
            if n > max_cubes[color]:
                max_cubes[color] = n
        start = end
        end = record.find(";", start+1)
        if end == -1:
            end = len(record)
    for color, n in TOTAL_CUBES.items():
        if max_cubes[color] > n:
            return 0
    return id



def main():
    with open(sys.argv[1], "r") as f:
        records = f.readlines()
    vals = [parse_game_record(r) for r in records]
    print(sum(vals))

if __name__ == "__main__":
    main()