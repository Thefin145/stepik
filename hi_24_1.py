print('определение % вхожднения в строку 2х заданных символов')

gen = input('введите строку- ')
nuc1 = input('введите искомый символ1- ')
nuc2 = input('введите искомое символ2- ')

print(float(gen.upper().count(nuc1) + gen.upper().count(nuc2)) / len(gen) * 100)