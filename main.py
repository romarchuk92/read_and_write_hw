
# Задача №1

import os
from pprint import pprint

# current = os.getcwd()
# file_name = 'recipes.txt'

# full_path = os.path.join(current,  file_name)
# with open(full_path, 'rt', encoding='utf-8') as file:
   
#     cook_book  = {}
    
#     for line in file:
#         dish_name = line.strip()
#         ingr_in_dish = int(file.readline().strip())
        
#         ingredients = []
        
#         for _ in range(ingr_in_dish):
#             ingr, quantity, unit = file.readline().strip().split('|')
#             ingredients.append({
#             'ingredient_name' : ingr,
#             'quantity' : quantity,
#             'measure' : unit
#             })
    
#         file.readline()
#         cook_book [dish_name] = ingredients
   
# pprint(cook_book, width=100, sort_dicts=False)




    
# Задача №2

# def get_shop_list_by_dishes(dishes, person_count):
#     for_persons = {}

#     for name, ingredient in cook_book.items():
      
#         if name in dishes:
         
#             for ingr in ingredient:

#                 if ingr['ingredient_name'] in for_persons:
#                     for_persons[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count
                                               
#                 else:
#                     for_persons[ingr['ingredient_name']] = {'meassure' : ingr['measure'], 'quantity' :  int(ingr['quantity']) * person_count}

#     return for_persons


# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)




# Задача №3

import os
folder_path = r"C:\Users\Admin\Desktop\read-and-write\txt"
#список адресов файлов в папке "txt"
file_paths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]
file_result = 'result.txt'
#список файлов в папке "txt"
my_files = os.listdir(folder_path)
#создаем список для загрузки данных из файлов
common_txt_file_list = []

#делаем цикл по списку имен файлов
for file_name in my_files:
  with open(f'{folder_path}\{file_name}', 'r', encoding="utf8") as f:
     file_lines = f.readlines()
     #добавляем данные по файлу 
     common_txt_file_list.append([str(len(file_lines)), file_name, file_lines])

#сортировка списка
sort_common_txt_file_list = sorted(common_txt_file_list)

#запись отсортированного списка в файл result.txt
for lists in sort_common_txt_file_list:
    
    with open(file_result, "a", encoding="utf8") as file:
        file.write('\n' + str(lists[1]) + '\n')
        file.write(str(lists[0]) + '\n')
        
        for text_list in lists[2]:
          file.writelines(text_list)






