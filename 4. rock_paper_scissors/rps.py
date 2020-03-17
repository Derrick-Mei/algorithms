#!/usr/bin/python

import sys
"""
base case - n == 1, return ['rock], ['paper], ['scissors]
"""


def rock_paper_scissors(n):
    baseArr = [['rock'], ['paper'], ['scissors']]

    if n == 0:
        return [[]]

    while n > 1:
        tempArr = [[]] * len(baseArr)*3
        for i in range(len(baseArr)):
            print(f'i: {i}')
            rock = baseArr[i][:]
            paper = baseArr[i][:]
            scissors = baseArr[i][:]
            rock.append('rock')
            paper.append('paper')
            scissors.append('scissors')
            tempArr[i*3+0] = rock
            tempArr[i*3+1] = paper
            tempArr[i*3+2] = scissors
        baseArr = tempArr
        n -= 1
    return baseArr


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
