def expt_iter(base, power):
    """ Implements the exponent function iteratively
    >>> expt_iter(2, 3)
    8
    >>> expt_iter(4, 0)
    1
    """
    result, count = 1, 0
    while count < power:
        result, count = result * base, count + 1
    return result

def expt_rec(base, power):
    """ Implements the exponent function recursively
    >>> expt_rec(3, 2)
    9
    """
    return base * expt_rec(base, power - 1) if power > 0 else 1

def count_stair_ways(n):
    return count_stair_ways(n - 1) + count_stair_ways(n - 2) if n > 1 else 1

def paths(m, n):
    """
    >>> paths(2, 2)
    2
    >>> paths(117, 1)
    1
    """
    return paths(m - 1, n) + paths(m, n - 1) if m > 1 and n > 1 else 1

def has_sum(total, n1, n2):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0(3) + 1(5) = 5
    True
    >>> has_sum(11, 3, 5) # 2(3) + 1(5) = 11
    True
    """
    if total > 0:
        return has_sum(total - n1, n1, n2) or has_sum(total - n2, n1, n2)
    elif total == 0:
        return True
    return False

def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer A prints within this range
    True
    >>> sum_range(40, 55) # Printer A can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer A + Printer B will print
    ...           # somewhere between 180 and 200 copies total
    True
    """
    if lower > upper or upper < 0:
        return False
    if lower <= 0 and upper >= 0:
        return True
    return sum_range(lower - 50, upper - 60) or sum_range(lower - 130, upper - 140)
