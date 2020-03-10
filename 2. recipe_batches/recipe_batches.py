#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    lowestBatch = None

    for key, value in recipe.items():

        if key not in ingredients:
            return 0

        batchSize = ingredients[key]//value

        if lowestBatch == None or batchSize < lowestBatch:
            lowestBatch = batchSize

    return lowestBatch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
