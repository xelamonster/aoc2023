#!/usr/bin/env python3
import math
import re
import sys

def get_steps(network, directions, node):
    steps = 0
    while not node.endswith("Z"):
        d = directions[steps % len(directions)]
        i = 0 if d == "L" else 1
        node = network[node][i]
        steps += 1
    return steps

def main():
    with open(sys.argv[1], "r") as f:
        data = f.readlines()
    directions = data[0].strip()
    pattern = re.compile(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)")
    groups = [pattern.match(l).groups() for l in data[2:]]
    network = {
        g[0]: (g[1], g[2]) for g in groups
    }
    nodes = network.keys()
    locs = [n for n in nodes if n.endswith("A")]
    steps = [get_steps(network, directions, n) for n in locs]
    print(math.lcm(*steps))

if __name__ == "__main__":
    main()    