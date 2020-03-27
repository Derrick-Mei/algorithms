#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])



hash = {}

def knapsack_hash(items, capacity):
    if len(items) == 0:
        return 0

    elif items[-1][1] > capacity:
        answer = knapsack_hash(items[:-1], capacity)
        hash[(len(items), capacity)] = answer
        return answer

    else:
        take = items[-1][2] + knapsack_hash(items[:-1], capacity-items[-1][1])
        no_take = knapsack_hash(items[:-1], capacity)
        answer = max(take, no_take)
        hash[(len(items), capacity)] = answer
        return answer


def list_finder(items, starting_capacity, max_value):
    remaining_value = max_value
    remaining_capacity = starting_capacity
    storage = []

    while remaining_value > 0:

        for i in range(1, len(items)+1):
            cur_val = hash.get((i, remaining_capacity), None)
            if cur_val != None and cur_val == remaining_value:
                storage.insert(0, i)
                remaining_capacity -= items[i-1][1]
                remaining_value -= items[i-1][2]
                break

    return storage


def lambda_recursive_knapsack(items, capacity):

    hash = {}

    max_value = knapsack_hash(items, capacity)

    items_taken = list_finder(items, capacity, max_value)

    print(f'max_value: {max_value}, storage: {items_taken}')

    return {"Value": max_value, "Chosen": items_taken}


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
        print(lambda_recursive_knapsack(items, capacity))
    else:
        print('Usage: recursive_knapsack.py [filename] [capacity]')
