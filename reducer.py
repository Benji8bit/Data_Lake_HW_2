### Reduce step for mapreduce ###
#
# with open('keywords_sorted.csv', encoding='UTF-8') as f:
#     for i, line in enumerate(f):
#         keyword, one = line.strip().split(',')
#         print(keyword, one)
#
#         if i > 8:
#             break

previous_keyword = None
keyword_count = 0

with open('keywords_sorted.csv', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        keyword, one = line.strip().split(',')
        one = int(one)

        if previous_keyword:
            if previous_keyword == keyword:
                keyword_count += one
            else:
                print(previous_keyword, keyword_count)
                keyword_count = one
                previous_keyword = keyword

        else:
            previous_keyword = keyword
            keyword_count = one

print(previous_keyword, keyword_count)