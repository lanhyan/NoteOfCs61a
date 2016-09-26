def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n % 2 == 0:
        n = n // 2
    elif n != 1:
        n = n * 3 + 1
    else:
        return 1
    return 1 + hailstone(n)


def symmetric(l):
    """Returns whether a list is symmetric.
    >>> symmetric([])
    True
    >>> symmetric([1])
    True
    >>> symmetric([1, 4, 5, 1])
    False
    >>> symmetric([1, 4, 4, 1])
    True
    >>> symmetric(['l', 'o', 'l'])
    True
    """
    "*** YOUR CODE HERE ***"
    if len(l) <= 1:
        return True
    elif l[0] == l[-1]:
        return symmetric(l[1: -1])
    else:
        return False
