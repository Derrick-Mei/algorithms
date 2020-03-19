#!/usr/bin/python

import sys


# Dynamic implementation
def making_change(amount, denominations):

    print(f"amount: {amount}, denominations: {denominations}")
    #  Edge cases
    if amount == 0 or denominations == None or len(denominations) == 0:
        return 0

    # make an array to hold vars
    arr = [0] * (amount+1)

    arr[0] = 1  # there's 1 way of making change for 0 change

    #  The big logic is here.  So if we have different denominations of coins
    # there's 1 way to make change using pennies
    # anything after that, lets say with pennies, nickels, and dimes.  There are 2 ways to make 5 cents.  5-pennies or a nickle
    # 10 cents we can have all the 5-cent combos plus a nickle.
    # then you have to loop over using the same logic with dimes and so forth although order does not matter.

    # Loop over all denominations
    for coin in denominations:

        # Loop over arr, so that each value in array is adding the arr[i - denominationValue]
        for j in range(coin, amount+1):
            arr[j] += arr[j - coin]

        print(f"arr: {arr}")

    return arr[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
