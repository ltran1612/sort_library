from sort import *
sort = quick_sort

def test(list, name):
    print(name)

    sort(list, SMALL_BIG)
    print(list)

    sort(list, BIG_SMALL)
    print(list)

    print("")

small_big = [1, 2, 3, 4, 5, 6]
big_small = [6, 5, 4, 3, 2, 1]
duplication = [1, 2, 3, 4, 3, 6, 5, 5]
negative = [-1, -2, 3, 34, -2, 39, 34, 0]
empty = []
single = [1]

# small big
test(small_big, "small_big")

# big_small
test(big_small, "big_small")

# duplication
test(duplication, "duplication")

# negative
test(negative, "negative")

# empty
test(empty, "empty")

# single
test(single, "single")