# Цветовая схема для вывода в терминал

GREEN = '\033[0;32m'
NC = '\033[0m'


print(GREEN + "\nРабота со словарями " + NC)
print("Создадим словарь с несколькими парами ключ-значение")
my_dict = {"Vasya": 1975, "Egor": 1999, "Masha": 2002}
print("\nDict:", my_dict)

print("\nПопробуем обратиться к существующей паре 'Masha'и несуществующей паре 'Pavel', используя метод get()")
print("\nExisting value:", my_dict.get("Masha"))
print("Not existing value:", my_dict.get("Pavel"))

# Добавление двух новых пар ключ-значение
my_dict["Kamila"] = 1981
my_dict["Artem"] = 1915
print("\nДобавим в словарь две новые пары значений: 'Kamila: 1981' и 'Artem: 1915'\n\n", my_dict)


print("\nУдалим существующую пару 'Artem' используя метод 'pop'")
deleted_value = my_dict.pop("Artem")
print("\nDeleted value:", deleted_value)

print("\nВыводим словарь после её удаления\n")
print("Modified dictionary:", my_dict)

print(GREEN + "\nРабота с множествами " + NC)

print("Создадим множество my_set с разными типами данных и повторяющимися значениями")
my_set = {1, "Яблоко", 42.314}
print("\nSet:", my_set)

print("\nДобавим в него два новых элемента 13 и (5, 6, 1.6) используя метод 'add'\n")
my_set.add(13)
my_set.add((5, 6, 1.6))

print(my_set)

my_set.discard('Яблоко')
print("\nУдалим элемент множества используя метод 'discard': my_set.discard('Яблоко')")
# Вывод множества после изменений
print("\nModified set:", my_set)
