from random import randint


def slice_list(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def get_random_list(max_len):
    low_upper_bound = 1
    high_upper_bound = 9
    return [randint(1, randint(low_upper_bound, high_upper_bound)) for i in range(max_len)]
