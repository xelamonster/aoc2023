#!/usr/bin/env python3
import sys

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
            n = int(r[0].strip())
            color = r[1].strip()
            if n > max_cubes[color]:
                max_cubes[color] = n
        start = end
        end = record.find(";", start+1)
        if end == -1:
            end = len(record)
    return max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]



def main():
    with open(sys.argv[1], "r") as f:
        records = f.readlines()
    vals = [parse_game_record(r) for r in records]
    print(sum(vals))

if __name__ == "__main__":
    main()