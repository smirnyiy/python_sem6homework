# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint

number = int(input('Введите количество элементов списка: '))

list_of_nums = [randint(0, 10) for i in range(number)]
print(list_of_nums)
new_list = [i for i in list_of_nums if list_of_nums.count(i)==1]
print('Список неповторяющихся элементов:')
print(new_list)