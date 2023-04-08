
# Задача №1

import os
from pprint import pprint

current = os.getcwd()
file_name = 'recipes.txt'

full_path = os.path.join(current,  file_name)
with open(full_path, 'rt', encoding='utf-8') as file:
    
    cook_book  = {}
    
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
        cook_book [dish_name] = ingredients
   
# pprint(cook_book, width=100, sort_dicts=False)




    
# Задача №2

def get_shop_list_by_dishes(dishes, person_count):
    for_persons = {}

    for name, ingredient in cook_book.items():
      
        if name in dishes:
         
            for ingr in ingredient:

                if ingr['ingredient_name'] in for_persons:
                    for_persons[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count
                                               
                else:
                    for_persons[ingr['ingredient_name']] = {'meassure' : ingr['measure'], 'quantity' :  int(ingr['quantity']) * person_count}

    return for_persons


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)



