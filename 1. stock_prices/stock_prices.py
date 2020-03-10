#!/usr/bin/python

import argparse


def find_max_profit(prices):

    if len(prices) < 2:
        return None
        
    lowest = prices[0]
    biggestDifference = prices[1] - prices[0]

    for i in range(1, len(prices)):
        currentDifference = prices[i] - lowest
        if currentDifference > biggestDifference:
            biggestDifference = currentDifference
        if prices[i] < lowest:
            lowest = prices[i]
    return biggestDifference


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
