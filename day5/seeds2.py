#!/usr/bin/env python3
import sys

class AlmanacMap:
    def __init__(self, lines):
        self.name = lines[0].split()[0]
        name_tokens = self.name.split("-")
        self.src = name_tokens[0]
        self.dest = name_tokens[2]
        self.src_ranges = []
        self.dest_ranges = []
        for line in lines[1:]:
            dest_start, src_start, size = [int(x) for x in line.split()]
            self.src_ranges.append((src_start, src_start+size))
            self.dest_ranges.append((dest_start, dest_start+size))
    
    def translate(self, x):
        for i, r in enumerate(self.src_ranges):
            if x >= r[0] and x < r[1]:
                offset = x - r[0]
                return self.dest_ranges[i][0] + offset
        return x
    
    def translate_reverse(self, x):
        for i, r in enumerate(self.dest_ranges):
            if x >= r[0] and x < r[1]:
                offset = x - r[0]
                return self.src_ranges[i][0] + offset
        return x

def main():
    with open(sys.argv[1], "r") as f:
        almanac = f.readlines()
    seed_vals = [int(n) for n in almanac[0][almanac[0].find(":")+1:].strip().split()]
    seed_ranges = []
    s = 0
    while s + 1 < len(seed_vals):
        seed_ranges.append((seed_vals[s], seed_vals[s] + seed_vals[s+1]))
        s += 2
    l = 1
    almanac_maps = {}
    while l < len(almanac):
        if almanac[l].strip() == "":
            l += 1
            continue
        if almanac[l].strip()[-1] == ":":
            section_start = l
            while l < len(almanac) and almanac[l].strip() != "":
                l += 1
            almanac_map = AlmanacMap(almanac[section_start:l])
            almanac_maps[almanac_map.dest] = almanac_map
        else:
            raise RuntimeError("input not recognized: " + almanac[l])
    loc = 0
    while True:
        dest = "location"
        v = loc
        while dest != "seed":
            almanac_map = almanac_maps[dest]
            v = almanac_map.translate_reverse(v)
            dest = almanac_map.src
        for r in seed_ranges:
            if v >= r[0] and v < r[1]:
                print(loc)
                return
        loc += 1
    

if __name__ == "__main__":
    main()