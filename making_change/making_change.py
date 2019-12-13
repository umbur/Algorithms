#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # defined x which is a possible values the amount should be calculated 
  x = [1, 5, 10, 25]
  # if amount(10) is equal or less than the most biggest x then do the following:
  # 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")