GREEN = '\033[0;32m'
NC = '\033[0m'


# Данные по ученикам и их оценкам
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в отсортированный список для соответствия порядку оценок
sorted_students = sorted(students)  # ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']

# Создаем словарь с результатами
average_grades = {}

# Проходим по каждому ученику и его оценкам
for i, student in enumerate(sorted_students):
    # Извлекаем оценки конкретного ученика
    student_grades = grades[i]
    # Рассчитываем средний балл
    average_grade = sum(student_grades) / len(student_grades)
    # Добавляем в словарь среднего балла
    average_grades[student] = average_grade

# Выводим результат
print("\n", f"{GREEN}{average_grades}{NC}") # {'Johnny': 4.0, 'Bilbo': 3.0, 'Steve': 4.0, 'Khendrik': 4.0, 'Aaron': 4.0}
