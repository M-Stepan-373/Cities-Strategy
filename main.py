cities = {
    'London': [3],
    'Edinburg': [2],
    'Dublin': [1],
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
        print('0 - end turn')
        for i, name in enumerate(cities):
            print(i + 1, '-', name)
        choice = int(input())
        if choice == 0:
            resources['food'] += sum(
                val[0]
                for val in cities.values()
            )
        number = 1
        for i in cities:
            if number == choice:
                review = 'city_' + i
                break
            number += 1
        print()

    if review.startswith('city'):
        city_name = review.split('_')[1]
        print(city_name)
        print(f'Население:{cities[city_name][0]}')
        print('0 - назад')
        print('1 - рост')
        choice = int(input())
        if choice == 0:
            review = 'all'
        if choice == 1:
            if resources['food'] > 4:
                cities[city_name][0] += 1
                resources['food'] -= 5
        print()
