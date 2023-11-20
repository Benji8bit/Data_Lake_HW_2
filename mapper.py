### Mapper for keywords.csv: split for keywords.csv and split for every keyword are here ###

with open('keywords.csv', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        keywords, shows = line.strip().split(',')

        print(keywords, shows)
        if i > 12:
            break

with open('keywords_after_mapper.csv', 'w', encoding='UTF-8') as f_mapper:
    with open('keywords.csv', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            keywords, shows = line.strip().split(',')
            for word in keywords.split():
                if word == 'keyword':
                    continue
                f_mapper.write(f'{word}, 1\n')

with open('keywords_after_mapper.csv', 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        keyword, counter = line.strip().split(',')

        print(keyword, counter)
        if i > 12:
            break