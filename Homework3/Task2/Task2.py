# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 6
# -> 5

array_length = int(input('Введите количество элементов в массиве: '))
arr = []
count = 1
for i in range(1, array_length+1):
    arr.append(i)
print(f'Массив {arr}')
num = int(input('Введите число X: '))
for i in range(1, array_length+1):
    if num <= 0:
        print('Вы ввели некорректное число, попробуйте еще раз')
    elif arr[i] == num:
        print(f'Вы ввели число из массива {arr[i]}')
        break
    elif arr[-1] < num:
        print(f'Самое близкое по величине число из массива: {arr[-1]}')
        break