#!/usr/bin/env python3
import sys

digits = "0123456789"

def parse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    gear_ratios = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "*":
                adjacents = []
                up = row - 1
                down = row + 2
                left = col - 1
                right = col + 2
                for r in range(up, down):
                    if r < 0 or r >= rows:
                        continue
                    start = left
                    end = left
                    for c in range(left, right):
                        if c < 0 or c >= cols:
                            continue
                        if c < end:
                            continue
                        if matrix[r][c] in digits:
                            start = c
                            end = c + 1
                            while start > 0 and matrix[r][start-1] in digits:
                                start -= 1
                            while end < cols and matrix[r][end] in digits:
                                end += 1
                            if matrix[r][start] in digits:
                                adjacents.append(int(matrix[r][start:end]))
                if len(adjacents) == 2:
                    gear_ratios.append(adjacents[0] * adjacents[1])
    return sum(gear_ratios)

def main():
    with open(sys.argv[1], "r") as f:
        matrix = [l.strip() for l in f.readlines()]
    print(parse_matrix(matrix))

if __name__ == "__main__":
    main()