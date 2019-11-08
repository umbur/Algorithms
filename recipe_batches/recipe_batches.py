#!/usr/bin/python

import math

# def recipe_batches(recipe, ingredients):
#   max_number = 0
#   limit = None
#   for key, value in recipe.items():
#     if key in ingredients:
#       number = ingredients[key] // recipe[key]
#       print(number)
#     else:
#       max_number= 0
#       break
#     if limit == None:
#       max_number = number
#       limit = max_number
#     else:
#       if number < limit:
#         limit = number


#   return max_number
def recipe_batches(recipe, ingredients):
    batches = []
    for ingredient in recipe:
        if ingredient in ingredients:
            amount = ingredients[ingredient] // recipe[ingredient]
            if amount < 1:
                return 0
            else:
                batches.append(math.floor(amount))
        else:
            return 0
    return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2, 'butter': 2, 'flour': 2 }
  ingredients = { 'milk': 10, 'butter': 4, 'flour': 4 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))