# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

number_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {number_list}")
def get_numbers(numb_list):
        new_number_list = []
        for i in numb_list: 
            if i not in new_number_list:
                new_number_list.append(i) 
        # new_number_list.sort() - если требуется сортируем
        print(f"Список из неповторяющихся элементов: {new_number_list}")
get_numbers(number_list)
