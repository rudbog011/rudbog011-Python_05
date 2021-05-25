print('Введите номер кармана:')
number = int(input())
remainder = number % 2
if number >= 1 and number <= 36:
    if (((number >= 1 and number <= 10) or (number >= 19 and number <= 28)) and remainder == 0) or (((number >= 11 and number <= 16) or (number >= 29 and number <= 36)) and remainder != 0):
        print('Черный')
    else:
        print('Красный')
else:
    if number == 0:
        print('зеленый')
    else:
        print('ошибка ввода')
