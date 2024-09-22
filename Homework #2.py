repeat = input(
    '\nДля рассчета среднего времени выполнения домашнего задания нажмите "y", или любую другую клавишу для выхода: \n')
while repeat.lower() == 'y':

    completed_homework = input('\nВведите количество выполненных домашних заданий в виде целого числа: \n')
    while True:
        try:
            completed_homework = int(completed_homework)
            break
        except ValueError:
            print('\nВведите количество выполненных домашних заданий в виде целого числа: \n')
            completed_homework = input()

    hours_spent = input('\nВведите количество затраченных часов в виде целого или дробного числа: \n')
    while True:
        try:
            hours_spent = float(hours_spent)
            break
        except ValueError:
            print('\nВведите количество затраченных часов в виде целого или дробного числа: \n')
            hours_spent = input()

    course_name = input('\nВведите название курса: \n')
    while not course_name:
        print('\nВведите название курса: \n')
        course_name = input()

    time_per_assignment = hours_spent / completed_homework
    print(
        f"Курс: {course_name}, всего выполнено домашних заданий: {completed_homework}, затрачено часов: {hours_spent}, среднее время выполнения: {time_per_assignment:.3f} часа.")

    repeat = input('\nДля повтора нажмите "y", или любую другую клавишу для выхода: \n')
