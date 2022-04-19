#!/usr/bin/env python3
"""Modules for argument parsing, arrays and tables."""
import argparse
import sys
import numpy as np
from tabulate import tabulate


def pretty_table(data):
    """Print results into pretty table."""
    headers = ["Line Number", "Line Number"]
    table = tabulate(data, headers, tablefmt="fancy_grid", floatfmt=".0f")
    print(table)


def process_lines(filepath, number):
    """Process each line and insert into top_x as required."""
    line_num = 1
    top_x = np.zeros((number, 2))
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            try:
                if int(line) >= top_x[0][0]:
                    top_x[0][0] = line
                    top_x[0][1] = line_num
                    top_x = np.sort(top_x, axis=0)
                line_num += 1
            except Exception as exception:
                print(exception)
                print("Line number: ", line_num)
    return top_x


# Parse command line args
parser = argparse.ArgumentParser(
    description="topX - Find the longest line/s in a file.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "-n", "--number", help="Output the last NUM lines, instead of the last 10"
)
parser.add_argument("-f", "--file", help="File to read content from.")
parser.parse_args(args=None if sys.argv[1:] else ["--help"])
args = parser.parse_args()

# init vars
def main():
    """Run the code."""
    top_x = process_lines(vars(args)["file"], int(vars(args)["number"]))
    pretty_table(top_x)


if __name__ == "__main__":
    main()
