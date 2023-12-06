#!/usr/bin/env python3
import sys

class AlmanacMap:
    def __init__(self, lines):
        self.name = lines[0].split()[0]
        name_tokens = self.name.split("-")
        self.src = name_tokens[0]
        self.dest = name_tokens[2]
        self.src_ranges = []
        self.dest_starts = []
        for line in lines[1:]:
            dest_start, src_start, size = [int(x) for x in line.split()]
            self.src_ranges.append((src_start, src_start+size))
            self.dest_starts.append(dest_start)
    
    def translate(self, x):
        for i, r in enumerate(self.src_ranges):
            if x >= r[0] and x < r[1]:
                offset = x - r[0]
                return self.dest_starts[i] + offset
        return x    

def main():
    with open(sys.argv[1], "r") as f:
        almanac = f.readlines()
    seeds = [int(n) for n in almanac[0][almanac[0].find(":")+1:].strip().split()]
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
            almanac_maps[almanac_map.src] = almanac_map
        else:
            raise RuntimeError("input not recognized: " + almanac[l])
    src = "seed"
    values = seeds
    while src != "location":
        almanac_map = almanac_maps[src]
        values = [almanac_map.translate(v) for v in values]
        src = almanac_map.dest
    print(min(values))

if __name__ == "__main__":
    main()