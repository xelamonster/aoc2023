#!/usr/bin/env python3
import sys

digits = "123456789"
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def get_first_digit(line):
    numbers_indexes = [(line.find(n), digits[i]) for i, n in enumerate(numbers)]
    numbers_indexes = [n for n in numbers_indexes if n[0] >= 0]
    numbers_indexes.sort(key=lambda n: n[0])
    digits_indexes = [(line.find(d), d) for d in digits]
    digits_indexes = [d for d in digits_indexes if d[0] >= 0]
    digits_indexes.sort(key=lambda d: d[0])
    if len(numbers_indexes) > 0 and numbers_indexes[0][0] < digits_indexes[0][0]:
        return numbers_indexes[0][1]
    return digits_indexes[0][1]

def get_last_digit(line):
    numbers_indexes = [(line.rfind(n), digits[i]) for i, n in enumerate(numbers)]
    numbers_indexes.sort(key=lambda n: n[0], reverse=True)
    digits_indexes = [(line.rfind(d), d) for d in digits]
    digits_indexes.sort(key=lambda d: d[0], reverse=True)
    if len(numbers_indexes) > 0 and numbers_indexes[0][0] > digits_indexes[0][0]:
        return numbers_indexes[0][1]
    return digits_indexes[0][1]

def get_calibration_val(line):
    val_str = get_first_digit(line) + get_last_digit(line)
    return int(val_str)

def main():
    input_path = sys.argv[1]
    with open(input_path, "r") as f:
        input = f.readlines()
    calibration_vals = [get_calibration_val(l) for l in input]
    print(sum(calibration_vals))

if __name__ == "__main__":
    main()
