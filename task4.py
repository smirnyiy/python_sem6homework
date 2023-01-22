# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите натуральное число: '))

if number == 0:
        print (0)
elif number == 1:
        print (1)
else:
    list = [i for i in range(2, number+1) if number%i == 0]
    print (list)