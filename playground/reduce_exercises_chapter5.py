from functools import reduce

a = [0, -5, 1, 2, 20, 3, 4, 12, 5, 6, 58, 7, 8, 9]

##reduce for finding a mix/max of sequence
def my_min_func(a, b):
    #print(a, b)
    return a if a < b else b


numbers = [3, 5, 2, 4, 7, 1]
# print(reduce(my_min_func, numbers))


# 3 largest values
# print(sorted(a, reverse=True)[:3])


# using reduce implement function find 5/n largest/smallest numbers in a sequence



def help_func(acc, nxt):
    print(acc, type(acc), len(acc))
    if len(acc) > 5:
        break
    if nxt not in acc:
        return acc + [nxt]


def five_largest_number(a):
    return list(reduce(help_func, sorted(a), []))

print(five_largest_number(a))


##Group words by length
# words = ["these", "are", "some", "words", "for", "grouping"]

# def dict_add(acc, nxt):
#     acc[len(nxt)] = acc.get(len(nxt), []) + [nxt]
#     return acc

# def group_by_length(words):
#     return dict(reduce(dict_add, words, {}))

# print(group_by_length(words))
