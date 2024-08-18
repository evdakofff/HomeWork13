import random

my_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(my_list)
print('Число в первом поле - ', n)
result = ""
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result += f'{i}{j}'
print(f'Пароль для числа - {result}')
