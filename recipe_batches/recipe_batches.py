#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  for key, value in recipe.items():
    if key not in ingredients or ingredients[key] < value:
      batches = 0
      break
    temp = ingredients[key] // value
    if batches > 0 and temp > batches:
      continue
    batches = temp
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))