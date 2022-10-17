cities = {
    'London': [3, 0],
    'Edinburg': [2, 0],
    'Dublin': [1, 0],
}

review = 'all'

resources = {
    'wood': 5,
    'food': 10,
}

while True:
    if review == 'all':
        for name, amount in resources.items():
            print(name, '=', amount)
        print()
        print('0 - New City')
        print('1 - End turn')
        for i, name in enumerate(cities):
            print(i + 2, '-', name)
        choice = int(input())

        if choice == 0:
            if resources['wood'] > 9:
                resources['wood'] -= 10
                cities[input('Name City:\n')] = [1, 0]

        if choice == 1:
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

        number = 2
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
