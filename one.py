# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def get_natur():
    num = int(input("Введите число: "))
    i = 2
    number_list = []
    while i <= num:
        if num % i == 0:
            number_list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа: {number_list}")
get_natur()