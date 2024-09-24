print('\nВведите любую строку, кроме пустого значения: \n')
my_string = input()
while not my_string:
    print('\nВведите любую строку, кроме пустого значения: \n')
    my_string = input()
print('\n')
print("Печатаем строку в верхнем регистре:", my_string.upper())
print("Печатаем строку в нижнем регистре:",my_string.lower())
print("Печатаем строку без пробелов:", my_string.replace(" ",""))
print("Печатаем первый символ строки:", my_string[0])
print("Печатаем последний символ строки:", my_string[-1])
print("Печатаем количество символов в строке:", len(my_string))
print("Задание выполнено")



