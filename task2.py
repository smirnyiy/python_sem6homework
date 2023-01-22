# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Решение через list comprehension
import math

number = int(input('Введите целое число: '))

def fact(n):
    f = 1
    l = 1
    while l <= n:
        f = f * l
        l += 1
    return f

list = [fact(i) for i in range (1, number+1) ]
list1 = [math.factorial(i) for i in range (1, number+1) ]

print(list)
print(list1)