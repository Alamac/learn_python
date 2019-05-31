# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???
name_counter = {}
for student in students:
  if name_counter.get(student['first_name'], False):
    name_counter[student['first_name']] += 1
  else:
    name_counter.update({student['first_name']: 1})
for student in name_counter:
  print(student, name_counter[student])

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

name_counter = {}
for student in students:
  if name_counter.get(student['first_name'], False):
    name_counter[student['first_name']] += 1
  else:
    name_counter.update({student['first_name']: 1})

most_common_name = max(name_counter, key=name_counter.get)
print('Самое частое имя среди учеников: {}'.format(most_common_name))

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
i = 0

for school_class in school_students:
  name_count = {}
  i += 1
  for student in school_class:
    if name_count.get(student['first_name'], False):
      name_count[student['first_name']] += 1
    else:
      name_count.update({student['first_name']: 1})
  most_common_name = (max(name_count, key=name_count.get))
  print('Самое частое имя в классе {}: {}'.format(i, most_common_name))

  

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

for school_class in school:
  class_name = school_class['class']
  boys_counter = 0
  girls_counter = 0
  for name in school_class['students']:
    if is_male.get(name['first_name']):
      boys_counter += 1
    else:
      girls_counter += 1
  print('В классе {} {} девочки и {} мальчика'.format(class_name,girls_counter, boys_counter))


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

for school_class in school:
  class_name = school_class['class']
  boys_counter = 0
  girls_counter = 0
  for name in school_class['students']:
    if is_male.get(name['first_name']):
      boys_counter += 1
    else:
      girls_counter += 1
  school_class['boys_counter'] = boys_counter
  school_class['girls_counter'] = girls_counter

max_boys_class = max(school, key=lambda x:x['boys_counter'])['class']
max_girls_class = max(school, key=lambda x:x['girls_counter'])['class']

print('Больше всего мальчиков в классе {}'.format(max_boys_class))
print('Больше всего девочек в классе {}'.format(max_girls_class))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a