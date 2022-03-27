print('вывод из списка повторяющихся символов')

list = [int(i) for i in input().split(' ')]
list.sort()
print(list)
list_ans = []  #  пустой список для вывода
i = 0
for i in range(len(list) - 1):  #  111
    if list[i] == list[i + 1] and list[i] not in list_ans:
        list_ans.append(list[i])
        i = i + 2
    else:
        i = i + 1
ans = str()
for i in list_ans:
    ans += str(i) + ' '
print(ans)

print('нажмите Ввод для выхода')
input()
