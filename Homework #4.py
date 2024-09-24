print('\nВведите любую строку, кроме пустого значения": \n')
my_string = input()
while not my_string:
    print('\nВведите любую строку, кроме пустого значения: \n')
    my_string = input()
print('\n')
print(my_string.upper()) #Печать строки в верхнем регистре
print(my_string.lower()) #Печать строки в нижнем регистре
print(my_string.replace(" ","")) #Убираем все пробелы в строке
print(my_string[0]) #Печать первого символа строки
print(my_string[-1]) #Печать последнего символа строки