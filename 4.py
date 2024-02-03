import csv


def get_middle_salary(t, l):
    """
    Функция для получения средней зарплаты для определенного типа трудоустройства

    t - тип трудоустройства
    l - список всех вакансий

    Возвращает среднюю зарплату для необходимого вида трудоустройства
    """
    s, c = 0, 0
    for i in l:
        if i["Work_Type"] == t:
            s += int(i["\ufeffSalary"])
            c += 1
    return s / c


def get_percent(cur, middle):
    """
    Функция для получения процента зарплаты от средней зарплаты для этого трудоустройства

    cur - данная зарплата
    middle - средняя зарплата в этом виде трудоустройства

    Возвращает процент зарплаты от средней зарплаты для этого трудоустройства
    """
    return round(int(cur) / middle * 100)


with open("vacancy.csv", encoding="utf-8") as f:  # открытие файла
    f_reader = csv.DictReader(f, delimiter=";")  # список вакансий
    data = list(f_reader)


middle_salary = {}
for i in data:
    # составление словаря со средними зарплатами для различных типов трудоустройства
    t = i["Work_Type"]
    if t not in middle_salary:
        middle_salary[t] = get_middle_salary(t, data)
    # запись процента зарплаты от средней зарплаты
    i["percent"] = str(get_percent(i["\ufeffSalary"], middle_salary[t])) + "%"


with open("vacancy_procent.csv", encoding="utf-8", mode="w") as f:  # открытие файла для записи
    # запись данных в новую табличку
    names = ["\ufeffSalary", "Work_Type", "Company_Size", "Role", "Company", "percent"]
    f_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
    f_writer.writeheader()
    f_writer.writerows(data)