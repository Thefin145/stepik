print('задача Счастливый билет abcdef, где сумма (abc) == сумма (def) ')

ticket = input('введите №билета из 6 цифр ')
part1 = int(ticket) // 1000  #выделение первых 3 чисел
num3 = part1 % 10
num1 = part1 // 100
num2 = (part1 % 100) // 10
print(num1, num2, num3)
part2 = int(ticket) % 1000  #выделение вторых 3 чисел
num6 = part2 % 10
num4 = part2 // 100
num5 = (part2 % 100) // 10
print(num4, num5, num6)
sum1 = num1 + num2 + num3
sum2 = num4 + num5 + num6
print(sum1, sum2)
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')
print('нажмите Ввод для выхода')
input()
