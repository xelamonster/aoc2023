#!/usr/bin/env python3
import sys

digits = "0123456789"

def get_calibration_val(line):
    line_digits = [c for c in line if c in digits]
    val_str = line_digits[0] + line_digits[-1]
    return int(val_str)

def main():
    input_path = sys.argv[1]
    with open(input_path, "r") as f:
        input = f.readlines()
    calibration_vals = [get_calibration_val(l) for l in input]
    print(sum(calibration_vals))

if __name__ == "__main__":
    main()
