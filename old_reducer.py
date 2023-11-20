### Reduce step for mapreduce ###

with open('cards_sorted.csv', encoding='UTF-16') as f:
    for i, line in enumerate(f):
        suit, value, one = line.strip().split(',')
        print(suit, value, one)

        if i > 8:
            break

previous_suit = None
suit_count = 0

with open('cards_sorted.csv', encoding='UTF-16') as f:
    for i, line in enumerate(f):
        suit, value, one = line.strip().split(',')
        one = int(one)

        if previous_suit:
            if previous_suit == suit:
                suit_count += one
            else:
                print(previous_suit, suit_count)
                suit_count = one
                previous_suit = suit

        else:
            previous_suit = suit
            suit_count = one

print(previous_suit, suit_count)