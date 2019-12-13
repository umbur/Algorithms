#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Defined a list to track number of batches
    batches = []
    # Looping through recipe and ingredients lists to find identical keys 
    # and then divide them to each other and return min value of the result(batches)
    for ingredient in recipe:
        if ingredient in ingredients:
            amount = ingredients[ingredient] // recipe[ingredient]
            if amount < 1:
                return 0
            else:
                batches.append(math.floor(amount))
                print(batches)
        else:
            return 0
    return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2, 'butter': 2, 'flour': 2 }
  ingredients = { 'milk': 10, 'butter': 4, 'flour': 4 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))