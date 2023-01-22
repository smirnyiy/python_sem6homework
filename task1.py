# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

number = int(input('Введите количество элементов списка: '))
# Создание списка с помощью list comprehension
list_of_nums = [randint(0, 50) for i in range(number)]
print(list_of_nums)
# Сортировка списка и сохранение только элементов с нечетных позиций
list_of_nums = [x for i, x in enumerate(list_of_nums) if i%2]
print(list_of_nums)
sum_result = sum(list_of_nums)
print(sum_result)