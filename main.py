import os
from pprint import pprint

current = os.getcwd()
file_name = 'recipes.txt'

full_path = os.path.join(current,  file_name)
with open(full_path, 'rt', encoding='utf-8') as file:
    dish = {}
    
    for line in file:
        dish_name = line.strip()
        ingr_in_dish = int(file.readline().strip())
        ingredients = []
        
        for _ in range(ingr_in_dish):
            ingr, quantity, unit = file.readline().strip().split('|')
            ingredients.append({
            'ingredient_name' : ingr,
            'quantity' : quantity,
            'measure' : unit
            })
    
        file.readline()
        dish[dish_name] = ingredients
   
    pprint(dish, width=100, sort_dicts=False)
    




