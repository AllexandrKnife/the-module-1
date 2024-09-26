# Цветовая схема для вывода в терминал
RED = '\033[0;31m'
ORANGE = '\033[0;33m'
GREEN = '\033[0;32m'
NC = '\033[0m'


def get_integers():
    while True:
        try:
            var_int_input = input('Введите целые числа через пробел:\n')
            return [int(x) for x in var_int_input.split()]
        except ValueError:
            print(RED + "Ошибка ввода! Пожалуйста, введите только целые числа." + NC)


def get_floats():
    while True:
        try:
            var_float_input = input('Введите дробные числа через пробел:\n')
            return [float(x) for x in var_float_input.split()]
        except ValueError:
            print(RED + "Ошибка ввода! Пожалуйста, введите только дробные числа." + NC)


def get_strings():
    while True:
        var_strr = input('Введите строки через пробел:\n').split()
        if var_strr:
            return var_strr
        else:
            print(RED + "Ошибка ввода! Пожалуйста, введите хотя бы одну непустую строку." + NC)


print(GREEN + '\nПрактическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"\n' + NC)

var_int = get_integers()
var_float = get_floats()
var_str = get_strings()

immutable_var = (var_int, var_float, var_str)  # Неизменяемый кортеж
mutable_list = list(immutable_var)  # Изменяемый список

print("\nСоздадим кортеж и список, затем попытаемся их изменить.")
print("\nImmutable tuple:", immutable_var)
print("Mutable list:", mutable_list, "\n")

print("Пытаемся изменить первый элемент внутри кортежа: immutable_var[0] = [1, 2, 3]")
try:
    immutable_var[0] = [1, 2, 3]
except TypeError as e:
    print(RED + "\n  Ошибка при попытке изменения кортежа:\n" + NC, "\n", e)
    print(GREEN + "\nКортежи неизменяемы, т.е. нельзя изменить значения их элементов после создания!" + NC)

# Изменяем элементы списка
mutable_list[0] = 10  # Меняем первый элемент списка
mutable_list.append('Modified')  # Добавляем в конец списка новый элемент
print(
    "\nПопытаемся изменить список:\n" + "\nПрисвоим первому элементу списка значение 10 и добавим в конце строку 'Modified'\n")
print(" mutable list[0] = 10\n", "mutable_list.append('Modified')\n")
print(mutable_list)
print(GREEN + "\nКак видим, список можно менять без проблем!" + NC)
