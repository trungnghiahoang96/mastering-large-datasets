from functools import reduce

xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 8, 2, 6, 2, 10, 4]
xs1 = ["A", "B", "C", "A", "A", "C", "A"]


def my_filter(xs):
    return list(reduce(lambda acc, x: acc + [x] if x % 2 == 0 else acc, xs, []))


print(my_filter(xs))



##create Counter/ Frequencies with reduce
def counter_dict(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc


def my_frequencies(xs):
    return dict(reduce(counter_dict, xs, {}))


print(my_frequencies(xs1))
