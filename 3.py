import csv


def linear_search(x, l):
    """
    Функция, осуществляющая линейный поиск по списку вакансий

    x - искомое название компании
    l - список словарей вакансий

    Возвращает список индексов найденных вакансий или пустой список, если такой компании нет в списке.
    """
    i = 0
    res = []
    while i < len(l):
        if l[i]["Company"] == x:
            res.append(i)
        i += 1
    return res if res else []


with open("vacancy.csv", encoding="utf-8") as f:  # открытие файла
    f_reader = csv.DictReader(f, delimiter=";")  # список вакансий
    data = list(f_reader)
    s = input()
    while s != "None":
        ind = linear_search(s, data)  # поиск нужных вакансий
        if ind:
            for j in ind:
                salary = data[j]['\ufeffSalary']
                print(f"В {s} найдена вакансия: {data[j]['Role']}. З/п составит: "
                      f"{salary}")  # вывод в необходимом формате
        else:
            print("К сожалению, ничего не удалось найти")
        s = input()