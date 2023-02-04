# Задача №2:
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2

from random import randint

firstNum = randint(0, 1001) 
secondNum = randint(0, 1001)
sum = firstNum + secondNum
prod = firstNum * secondNum
print(f'Загадано два числа.\nСумма этих чисел равна {sum}.\n'f'Произведение этих чисел равно {prod}.')

D = sum ** 2 - 4 * prod
firstNum = int(sum / 2 - D ** (0.5) / 2)
secondNum = int(sum / 2 + D ** (0.5) / 2)
print(f'Первое загаданное число {firstNum}, второе загаданное число {secondNum}.')