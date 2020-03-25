#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
"""
1. make baseDict to hold the highestValue possible for that weight and items
2. make matrix of capacity+1 long and len(items)+1 long // +1 so we can account for 0 items and 0 weight
3. each row represents a new item being added to the possibilities
4. in each row, the index represents the weight
5. Loop over each item on it's respective index
    1. check if item can be added to that weight
        1. if it can fit, compare (item.value + maxValue of remainder weight (by looking at previous row)) with maxValue of weight of previous row
        2. if item.value + remainder > than maxValue of that weight of previous row, overwrite
6. return value and items
"""


def knapsack_solver(items, capacity):

    matrix = [[{'value': 0, 'items': []} for x in range(capacity + 1)]
              for y in range(len(items) + 1)]
    # print(matrix)

    for item in items:
        # print('\n\n\n\n')
        # print(item)
        row = item[0]
        size = item[1]
        value = item[2]

        for i in range(1, capacity+1):
            # print(f'i-weight: {i}')
            previous_value = matrix[row-1][i]['value']
            previous_items = matrix[row-1][i]['items'].copy()

            current_dict = matrix[row][i]

            if i >= size:
                # print(f'i is >=: {i}, size: {size}')
                remainder_weight = i - size
                # print(f'rw: {remainder_weight}')

                remainder_value = matrix[row-1][remainder_weight]['value']
                remainder_items = matrix[row -
                                         1][remainder_weight]['items'].copy()
                # print(f'rv: {remainder_value}, ri: {remainder_items}')

                if (value + remainder_value) > previous_value:
                    current_dict['value'] = value + remainder_value
                    current_dict['items'] = remainder_items + [row]

                else:
                    current_dict['value'] = previous_value
                    current_dict['items'] = previous_items
                    # print(f'cdict: {current_dict}')

            else:
                current_dict['value'] = previous_value
                current_dict['items'] = previous_items

    # print(f'matrix: {matrix}')
    lastDict = matrix[len(items)][capacity]
    # print(f'lastDict: {lastDict}')
    return {"Value": lastDict['value'], "Chosen": lastDict['items']}


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
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
