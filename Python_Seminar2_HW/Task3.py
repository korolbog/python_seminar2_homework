# Задайте список (словарь не нужно выводить!)
# из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.



list = []
sum = 0
result = 0
n = int(input('Введите число: '))
for i in range(n):
    result = result + (1+1/n)**n
    print(result)
    list.append(round(result, 2))
    sum = sum + result
print(list)
print (round(sum ,2))