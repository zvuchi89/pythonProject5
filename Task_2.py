# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456


name = input('Введите Фамилию и Имя: ')
birthday = int(input('Ваш год рождения полностью:  '))
city = input('Город где вы проживаете: ')
mail = input('email: ')
telephone = int(input('Телефон: '))

result = map(str.lower, [name, birthday, city, mail, telephone])
print((f'\n {name}, {birthday} года рождения, проживает в городе {city},'
       f' email: {mail}:, телефон: {telephone}'))
