print('Введите номер кармана:')
number = int(input())
remainder = number % 2
if number >= 1 and number <= 36:
    if remainder == 0 and ((number >= 1 and number <= 10) or (number >= 19 and number <= 28)):
        print('Черный')
    if remainder != 0 and ((number >= 11 and number <= 18) or (number >= 29 and number <= 36)):
        print('Черный')
    if remainder != 0 and ((number >= 1 and number <= 10) or (number >= 19 and number <= 28)):
        print('Красный')
    if remainder == 0 and ((number >= 11 and number <= 18) or (number >= 29 and number <= 36)):
        print('Красный')
else:
    if number == 0:
        print('Зеленый')
    else:
        print('Ошибка ввода')
