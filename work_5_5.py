print('Введите общее количество задач k:')
k = int(input())
print('Введите количество задач выполняемые в день m')
m = int(input())
if k % m == 0:
    print(int(k / m))
else:
    print(int(k // m + 1))