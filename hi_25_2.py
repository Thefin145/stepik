print('список чисел и их сумма')

list = [int(i) for i in input().split(' ')]
list_ans = []  #  пустой список для накопления сумм чисел
sum = 0 #  сумма 
i = 0
for i in range(len(list) - 1):
    sum = list[i + 1] + list[i - 1]
    list_ans.append(sum)
    i = i + 1
if len(list) == 1:
    sum = list[0]
    list_ans.append(sum)
else:
    sum = list[0] + list[i - 1]
    list_ans.append(sum)
ans = str()
for i in list_ans:
    ans += str(i) + ' '
print(ans)

print('нажмите Ввод для выхода')
input()
