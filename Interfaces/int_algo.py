# int_algo.py
"""
Interface to interact with Algo functions (algortithms)
"""


import argparse

# custom modules
from Algorithms.Sorting.bubble import *

parser = argparse.ArgumentParser(description="Welcome to Algorithm Analyser")
parser.add_argument("--algo", nargs=1, type=str, metavar="algorithm",
                    help="define algorithm name")
parser.add_argument("--list", nargs="*", type=str, metavar="list",
                    help="unsorted list of integers 1,2,3,4...")
parser.add_argument("--sort", nargs=1, type=str, metavar="ASC, DESC",
                    help="sorting type can be ASC or DESC")
parser.add_argument("--exit", nargs=0, required=False,
                    help="To exit Algorithm Analyser")
args = parser.parse_args()

# arguments processing
# convert input list to a list of integers
_list = [int(item) for item in args.list[0].split(",")]

# sorting algorithms
if args.algo[0] and args.sort[0]:
    # get algorithm name
    if args.algo[0] == "bubble":
        print("Calling bubble algorithm")
        _list = bubble(_list, args.sort[0])
        print("sorted list: ", _list)
    else:
        print("Unknown algorithm name")
