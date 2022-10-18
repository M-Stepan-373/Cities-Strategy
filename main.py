cities = {
    'Moskva': [1, 0],
}

review = 'all'

resources = {
    'wood': 5,
    'food': 10,
}

while True:
    if review == 'all':
        print('Total adult people -', sum(
            val[0]
            for val in cities.values()
        ))
        for name, amount in resources.items():
            print(name, '=', amount)
        print()
        print('0 - End turn')
        print('1 - New City')
        print('2 - Rules')


        for i, name in enumerate(cities):
            print(i + 3, '-', name)
        choice = int(input())

        if choice == 2:
            print('''
Есть города, а также два ресурса - еда и дерево.
У городов есть население взрослое, и молодое,
заплатив 5 еды можно увеличить молодое
население на 1, при этом молодого населения
не может быть больше взрослого населения : 2
с округлением в большую сторуну. Также можно
создать новый город, это требует 10 дерева,
в нём будет сразу 1 взрослое население. В конце
хода за каждое взрослое население будет на 1
возростать дерево и еда, также всё молодое
население станет взрослым.''', end='')
            input()

        if choice == 1:
            if resources['wood'] > 9:
                resources['wood'] -= 10
                cities[input('Name City:\n')] = [1, 0]

        if choice == 0:
            resources['food'] += sum(
                val[0]
                for val in cities.values()
            )

            resources['wood'] += sum(
                val[0]
                for val in cities.values()
            )

            for i in cities.values():
                i[0] += i[1]
                i[1] = 0

        number = 3
        for i in cities:
            if number == choice:
                review = 'city_' + i
                break
            number += 1
        print()

    if review.startswith('city'):
        city_name = review.split('_')[1]
        print(city_name)
        print(f'Adult people: {cities[city_name][0]}')
        print(f'Young people: {cities[city_name][1]}')
        print('0 - back')
        print('1 - grow')
        choice = int(input())

        if choice == 0:
            review = 'all'

        if choice == 1:
            if resources['food'] > 4 and cities[city_name][0] // 2 + cities[city_name][0] % 2 > cities[city_name][1]:
                cities[city_name][1] += 1
                resources['food'] -= 5
        print()
