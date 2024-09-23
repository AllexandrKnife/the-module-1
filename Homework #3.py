# Запрашиваем имя пользователя
name = input("Введите ваше имя: ")

# Запрашиваем возраст и преобразуем его в целое число
# Проверяем ввод на корректность

while True:
    age = input("Введите ваш прежний возраст (целое число лет): ")
    try:
        age = int(age)
        if age >= 0:
            break
        else:
            print("Возраст не может быть отрицательным.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Запрашиваем число для изменения возраста и добавляем его к возрасту
# Проверяем ввод на корректность

while True:
    additional_years = input("Введите количество лет, на которое хотите изменить возраст (целое число): ")
    try:
        additional_years = int(additional_years)
        if additional_years >= 0:
            break
        else:
            print("Значение не может быть отрицательным.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

age = age + additional_years

# Запрашиваем статус студента, удаляем из строки ответа пробелы в начале и конце, переводим символы в нижний регистр

is_student_response = input(
    "Вы студент?  - Введите 'да', если студент и любое другое значение, если нет: ").strip().lower()

# Определяем логическое значение на основе ответа
is_student = is_student_response == "да"

print("\nName:", name)
print("Age:", age - additional_years)
print("New Age:", age)
print("Is Student:", is_student)
