print('печать всех введенных чисел, удовлетворяющим условию 10<=<=100 ')
i = 1
while i <= 5:
    a = int(input('a= '))
    if a < 100:
        break
    elif a < 10:
        continue
    elif 10 <= a <= 100:
        print(a)      
print('введите Ввод для выхода из программы')
input()