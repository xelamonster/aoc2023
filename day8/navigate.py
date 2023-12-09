#!/usr/bin/env python3
import re
import sys

def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
    directions = data[0].strip()
    pattern = re.compile(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")
    groups = [pattern.match(l).groups() for l in data[2:]]
    network = {
        g[0]: (g[1], g[2]) for g in groups
    }
    steps = 0
    loc = "AAA"
    while loc != "ZZZ":
        d = directions[steps % len(directions)]
        i = 0 if d == "L" else 1
        loc = network[loc][i]
        steps += 1
    print(steps)

if __name__ == "__main__":
    main()    