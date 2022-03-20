print('вывод среднего арифметического всех чисел отрезка, кратных 3')

num1 = int(input('введите а= '))
num2 = int(input('введите б= '))
s = 0  
d = 0  #счетчик слагаемых

for i in range(num1, num2 + 1):
    if i % 3 == 0:
        s += i
        d = d + 1
print(float(s / d))
input()