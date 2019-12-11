#!/usr/bin/python
# Initial commit
import argparse

def find_max_profit(prices):
  # Defined min_price which is the minimum value of the first and second indexes of prices list
  min_price = min(prices[0], prices[1])
  # Defined profit which is the difference between second and first indexes of the prices list
  profit = prices[1] - prices[0]
  # print(profit)

  # Starting a loop if the length of the prices list bigger than 2, if no returning the existing profit
  if len(prices) > 2:
    for i in range(2, len(prices)):
      if prices[i] - min_price > profit:
        profit = prices[i] - min_price
      if prices[i] < min_price:
        min_price = prices[i]
  return profit


print(find_max_profit([20,3,3,9,1,25]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()
# print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

