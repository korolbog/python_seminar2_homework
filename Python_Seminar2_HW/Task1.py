# Задача 1.
# Напишите программу,
# которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

n = float(input('Введите вещественное число: '))
temp1 = n
head_count = 0
while temp1 % 10 > 0:
    temp1 //= 10
    head_count += 1

head = int(n)
head_sum = 0
for i in range(head_count):
    head_sum += head % 10
    head //= 10

temp2 = str(n)
temp2 = temp2[head_count+1:len(temp2)]

tail = int(temp2)
temp3 = tail
tail_count = 0
while temp3 % 10 > 0:
    temp3 //= 10
    tail_count += 1

tail_sum = 0
for i in range(tail_count):
    tail_sum += tail % 10
    tail //= 10

print(f'Сумма цифр = {head_sum+tail_sum}')