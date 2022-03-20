print('список чисел и их сумма')

list = [int(i) for i in input().split(' ')]
list_ans = []  #  пустой список для накопления сумм чисел
s = 0 #  счетчик 
i = 0
for i in range(len(list) - 1):
    s = list[i + 1] + list[i - 1]
    list_ans.append(s)
    i = i + 1
if len(list) == 1:
    s = list[0]
    list_ans.append(s)
else:
    s = list[0] + list[i - 1]
    list_ans.append(s) 
i = 0
ans = str()
for i in range(len(list_ans) - 1):
    ans += str(list_ans[i]) + ' '
    i += 1
else:
    ans += str(list_ans[i])
print(ans)

print('нажмите Ввод для выхода')
input()
