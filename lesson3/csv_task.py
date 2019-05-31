import csv

dict_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', encoding='utf-8', newline='') as export:

    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(export, fields, delimiter=';')
    writer.writeheader()
    for user in dict_list:
        writer.writerow(user)