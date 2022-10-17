# Task 1. Напишите программу, которая принимает на вход
#  вещественное число и показывает сумму его цифр.

# number = str(input(' Введите число: '))
# sum = 0
# for symbol in number:
#     if symbol.isdigit():
#         sum += int(symbol)
# print(sum)


# Task 2. Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число: '))
# some_list = [1]
# fact = 1
# for i in range(2, n+1):
#     fact *=i
#     some_list.append(fact)
# print(some_list)


# Task 3. Задайте список из n чисел
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число: '))
# sum = 0
# for i in range (1, n+1):
#     sum += (1 + 1/i) **i
# print(sum)