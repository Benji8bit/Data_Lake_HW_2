### Mapper for cards.csv and requests.csv ###

with open('cards.csv', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        suit, value = line.strip().split(',')
        print(suit, value)

        if i > 5:
            break

SUITES = {
    'червы': 'H',
    'пики': 'S',
    'бубны': 'D',
    'трефы': 'C',
}

VALUES = {
    'валет': 'J',
    'дама': 'Q',
    'король': 'K',
    'туз': 'A',
}

with open('cards.csv', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        suit, value = line.strip().split(',')

        suit = SUITES[suit]

        if value in VALUES:
            value = VALUES[value]

        print(f'{suit}, {value}, 1')
        if i > 5:
            break

with open('cards_after_mapper.csv', 'w', encoding='UTF-8') as f_mapper:
    with open('cards.csv', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            suit, value = line.strip().split(',')

            suit = SUITES[suit]

            if value in VALUES:
                value = VALUES[value]

            if value.isdigit() and int(value) >= 6:
                f_mapper.write(f'{suit}, {value}, 1')