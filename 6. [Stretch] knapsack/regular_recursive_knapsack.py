#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def recursive_knapsack_solver(items, capacity, item_index):

    # If no more capacity or we're reached the end of the items, return 0
    if capacity <= 0 or item_index == len(items):
        return 0

    # if the items weight is > than capacity skip to next item
    if items[item_index][1] > capacity:
        return recursive_knapsack_solver(items, capacity, item_index+1)

    # right_max is if I take the item
    right_max = items[item_index][2] + recursive_knapsack_solver(items, capacity-items[item_index][1], item_index+1)

    # left_max is if I don't take the item
    left_max = recursive_knapsack_solver(items, capacity, item_index+1)

    return max(right_max, left_max)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(recursive_knapsack_solver(items, capacity, 0))
    else:
        print('Usage: recursive_knapsack.py [filename] [capacity]')
