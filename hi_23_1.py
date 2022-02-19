print('вывод таблицы умножения для чисел')
q = 1
num1 = int(input('введите а= '))
num2 = int(input('введите б= '))
num3 = int(input('введите в= '))
num4 = int(input('введите г= '))
num1 > 0
num3 > 0
num1 <= num2 <= 10
num3 <= num4 <= 10
for j in range(num3, num4 + q):
    print ('', j, end = '', sep = '\t')
for i in range(num1, num2 + q):
    print('\n', i, end = '')
    for j in range(num3, num4 + q):
        print('\t', j * i, end = '')           
print('\n','нажмите Ввод для выхода', end = '')
input()
