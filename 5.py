import csv
import random


with open("vacancy.csv", encoding="utf-8") as f:
    f_reader = csv.DictReader(f, delimiter=";")  # список всех вакансий
    data = list(f_reader)
    res = {}
    for i in data:
        # создание словаря с ключом название компании и значением - вакансиями
        company = i["Company"]
        title = i["Role"].capitalize()
        salary = i["\ufeffSalary"]
        work_type = i["Work_Type"].capitalize()
        if company not in res:
            res[company] = [f"({title}, {salary}, {work_type})"]
        else:
            res[company].append(f"({title}, {salary}, {work_type})")

    # Вывод всех вакансий для компании
    s = random.choice(list(res.keys()))
    print(f"Компания - {s}")
    print("Вакансии:")
    for i in res[s]:
        print(i)
    print()

    # Вывод компании с самым большим количеством вакансий
    company = sorted(res, key=lambda x: len(res[x]), reverse=True)[0]
    print(company)