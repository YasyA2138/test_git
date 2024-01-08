import random
b = []

for i in range(random.randint(5, 10)):
    a = int(input('Введите любое число до 100: '))
    b.append(a)
    b.sort()
    b.pop(b.count >= 100)

print('ВЕЛИКІ ЗМІНИ!!!')
print('ВЕЛИКІ ЗМІНИ!!!')
print('ВЕЛИКІ ЗМІНИ!!!')
print('Вы вели не так числа, и мы их рассортировали', b)
print('ВЕЛИКІ ЗМІНИ!!!')
print('ВЕЛИКІ ЗМІНИ!!!')
print('ВЕЛИКІ ЗМІНИ!!!')