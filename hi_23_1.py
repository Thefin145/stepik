print('вывод таблицы умножения для чисел от 1 до 10')
num1 = int(input('введите а= '))
num2 = int(input('введите б= '))
num3 = int(input('введите в= '))
num4 = int(input('введите г= '))
if (num1 < 0 or num3 < 0) or (num2 > 10 or num4 > 10) or (num1 > num2 or num3 > num4):
    print('заверщение программы')
else:
    for j in range(num3, num4 + 1):
        print ('', j, end = '', sep = '\t')
    for i in range(num1, num2 + 1):
        print('\n', i, end = '')
        for j in range(num3, num4 + 1):
            print('\t', j * i, end = '')           
print('\n','нажмите Ввод для выхода', end = '')
input()
