import csv


with open("vacancy.csv", encoding="utf-8") as f:  # открытие файла
    f_reader = csv.DictReader(f, delimiter=";")  # список вакансий
    data = list(f_reader)


# создание словаря с ключом название компании и
# значением - вакансия самой высокооплачиваемой профессии в компании
data_new = {}
for i in data:
    company = i["Company"]
    if company in data_new:
        data_new[company] = max(data_new[company], i, key=lambda x: int(x["\ufeffSalary"]))
    else:
        data_new[company] = i


with open("vacancy_new.csv", mode="w", encoding="utf-8") as f:  # открытие файла для записи
    names = ["company", "role", "Salary"]  # заголовки
    f_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)

    # создание данных для новой таблицы
    res = []
    for i in data_new:
        res.append({"company": i, "role": data_new[i]["Role"], "Salary": data_new[i]["\ufeffSalary"]})
    f_writer.writeheader()
    f_writer.writerows(res)

    for i in sorted(res, key=lambda x: int(x["Salary"]), reverse=True)[:3]:
        print(f"{i['company']} - {i['role']} - {i['Salary']}")  # вывод в необходимом формате