print('печать всех введенных чисел, удовлетворяющим условию 10<=<=100 ')

while True:
    input_number = int(input('a= '))
    if input_number < 100:
        break
    elif input_number < 10:
        continue
    elif 10 <= input_number <= 100:
        print(input_number)        
print('введите Ввод для выхода из программы')
input()
