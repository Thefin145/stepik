print('задача Счастливый билет abcdef, где сумма (abc) == сумма (def) ')

ticket = input('введите №билета из 6 цифр ')
part1 = int(ticket) // 1000  #выделение первых 3 чисел
c = part1 % 10
a = part1 // 100
b = (part1 % 100) // 10
print(a, b, c)
part2 = int(ticket) % 1000  #выделение вторых 3 чисел
f = part2 % 10
d = part2 // 100
e = (part2 % 100) // 10
print(d, e, f)
sum1 = a + b + c
sum2 = d + e + f
print(sum1, sum2)
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
print('нажмите Ввод для выхода')
input()