#!/usr/bin/env python3.6

import argparse
import sys

# build the parser
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

# parse the arguments
args = parser.parse_args()
try:
    f = open(args.filename)
    limit =args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
#except:
#    print("Testing")
else:
    # read the file, reverse the contens and print
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
#finally:
#    print("Finally")
