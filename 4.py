# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, 
# вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

import os
os.system('cls||clear')

with open("task2\\file.txt", "r") as f:  
    a = f.read().split('\n')
print(a)

arrayList = []
n = int(input('Введите число N: '))

for i in range(-n, n+1):               
    arrayList.append((i))
print(arrayList)

print(type(a[0]))

res = 1
for item in a: 
    res *= arrayList[int(item)]

print(res)