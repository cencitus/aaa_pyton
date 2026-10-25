import csv


def read_employees() -> list:
    """
    Читает CSV-файл и возвращает список сотрудников
    """
    table = []
    with open('Corp_Summary.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            table.append(row)
    return table[1::]


def get_department_hierarchy(table: list) -> dict:
    """
    Группирует отделы по департаментам.
    Отделы уникальны
    """
    departments = {}
    for row in table:
        department = row[1]
        division = row[2]
        if department not in departments:
            departments[department] = []
        if division not in departments[department]:
            departments[department].append(division)
    return departments


def print_first_report(departments: dict) -> None:
    """
    Выводит департаменты и входящие в них отделы
    """
    for department, divisions in departments.items():
        print(department, '\n   ', ', '.join(divisions))


def summary_by_department(table: list) -> dict:
    """Группирует зарплаты сотрудников по департаментам."""
    salaries_by_department = {}
    for row in table:
        department = row[1]
        salary = int(row[5])
        if department not in salaries_by_department:
            salaries_by_department[department] = []
        salaries_by_department[department].append(salary)
    return salaries_by_department


def calculate_statistics(salaries_by_department: dict) -> dict:
    """Рассчитывает статистику по департаменту"""
    statistics = {}
    for department, salaries in salaries_by_department.items():
        employee_count = len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
        avg_salary = sum(salaries) / employee_count
        statistics[department] = {'count': employee_count, 'min_salary': min_salary,
                                  'max_salary': max_salary, 'avg_salary': avg_salary}

    return statistics


def print_second_report(statistics: dict) -> None:
    """Выводит второй отчет по департаментам"""
    for department, data in statistics.items():
        print(
            f'Департамент: {department}\n'
            f'Количество сотрудников: {data["count"]}\n'
            f'Вилка зарплат: {data["min_salary"]} - {data["max_salary"]}\n'
            f'Средняя зарплата: {data["avg_salary"]:.2f}\n')


def save_report(statistics: dict) -> None:
    """Сохраняет второй отчт в CSV"""
    with open('report.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Департамент',
            'Количество сотрудников',
            'Вилка зарплат',
            'Средняя зарплата'
        ])
        for department, data in statistics.items():
            writer.writerow([
                department,
                data['count'],
                f'{data["min_salary"]} - {data["max_salary"]}',
                round(data['avg_salary'], 2)
            ])


def main(variant: int) -> None:
    """Формирует отчёт по выбранному варику"""
    table = read_employees()
    if variant == 1:
        departments = get_department_hierarchy(table)
        print_first_report(departments)
    elif variant == 2:
        salaries = summary_by_department(table)
        statistics = calculate_statistics(salaries)
        print_second_report(statistics)
    elif variant == 3:
        salaries = summary_by_department(table)
        statistics = calculate_statistics(salaries)
        save_report(statistics)
        print('Отчет сохранен')
    else:
        print('Введите корректное число (от 1 до 3)')


if __name__ == '__main__':
    print('Доступные варианты отчетов:')
    print('1. Иерархия департаментов')
    print('2. Сводка по департаментам')
    print('3. Сохранение сводки в CSV')
    variant = input('Выберите отчёт. Для выхода введи 0.\n')
    while variant != '0':
        if variant in ('1', '2', '3'):
            main(int(variant))
        else:
            raise ValueError("Ошибка. Число должно быть от 1 до 3")
        variant = input('Выберите отчёт. Для выхода введи 0.\n')
