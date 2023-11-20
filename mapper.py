### Mapper for cards.csv and requests.csv ###

with open('cards.csv') as f:
    for i, line in enumerate(f):
        suit, value = line.strip().split(',')
        print(suit, value)

        if i > 5:
            break