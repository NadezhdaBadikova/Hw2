# 5'. Реализуйте алгоритм перемешивания списка.
import random

import os 
os.system('cls')

arrayList = ['first element ', 'second element ', '-69 ', 'ты кто? ', 'егерь', 'Hello world']
random.shuffle(arrayList)
print(f'Random 1 {arrayList}')
random.shuffle(arrayList)   
print(f'Random 2 {arrayList}')
random.shuffle(arrayList)
print(f'Random 3 {arrayList}')
random.shuffle(arrayList)
print(f'Random 4 {arrayList}')
random.shuffle(arrayList)
print(f'Random 5 {arrayList}')