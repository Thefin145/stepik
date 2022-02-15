print('задача счет суммы чисел, пока не выпадет 0 ')
s = 0
a = int(input('введите число '))
while a != 0:
   s += a
   a = int(input('введите число '))
   if a == 0:
       print(s)
print(s)
print('нажмите Ввод для выхода')
input()
