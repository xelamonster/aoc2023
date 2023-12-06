#!/usr/bin/env python3
import sys

digits = "0123456789"

def parse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    part_numbers = []
    for row in range(rows):
        end = 0
        for col in range(cols):
            if col < end:
                continue
            part_number = ""
            start = col
            while col < cols and matrix[row][col] in digits:
                part_number += matrix[row][col]
                col += 1
            end = col
            if part_number != "":
                adjacents = []
                up = row - 1
                down = row + 2
                left = start - 1
                right = col + 1
                for r in range(up, down):
                    if r < 0 or r >= rows:
                        continue
                    for c in range(left, right):
                        if c < 0 or c >= cols:
                            continue
                        adjacents.append(matrix[r][c])
                for a in adjacents:
                    if a != "." and a not in digits:
                        part_numbers.append(int(part_number))
                        break
    return sum(part_numbers)

def main():
    with open(sys.argv[1], "r") as f:
        matrix = [l.strip() for l in f.readlines()]
    print(parse_matrix(matrix))

if __name__ == "__main__":
    main()