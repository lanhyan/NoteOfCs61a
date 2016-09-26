def  is_even(x):
    return x % 2 == 0
def  is_greater_than_three(x):
    return x > 3
def  print_if(n, pred):
    """
    >>> # 0, 2, 4, 6 are  the non -negative  even  integers  less  than 8.
    >>> even_count = print_if(8, is_even)
    0
    2
    4
    6
    >>> even_count
    4
    >>> # 4, 5 are  greater  than 3 and  less  than 6.
    >>> range_count = print_if(6,  is_greater_than_three)
    4
    5
    >>> range_count
    2
    """
    a = 0
    for i in range(0, n):
        if pred(i):
            print(i)
            a += 1
    return a
