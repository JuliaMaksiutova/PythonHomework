# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def sum_num(A, B):
    A += 1
    B -= 1
    if B > 0:
        return sum_num(A, B)
    else:
        return A

A = int(input('Введите число A: '))
B = int(input('Введите число B: '))

print(f'Сумма А и Б равна {sum_num(A, B)}')