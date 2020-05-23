#!/usr/bin/python

import timeit
import argparse


def find_max_profit(prices):
    if len(prices) == 1 or len(prices) == 0:
        return 0

    minNum = prices[0]
    profit = prices[1] - prices[0]
    for price in prices:
        if price < minNum:
            minNum = price
        elif(profit < price - minNum and price - minNum != 0):
            profit = price - minNum
    return profit
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))


start = timeit.default_timer()
print(find_max_profit([100, 90, 80, 80, 50, 20, 10]))
stop = timeit.default_timer()

print('Time: ', stop - start)
