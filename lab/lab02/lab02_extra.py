"""Optional program for lab02 """

from lab02 import *

from operator import add, sub, mul

def foldl(s, f, start):
    """Return the result of applying the function F to the initial value START
    and the first element in S, and repeatedly applying F to this result and
    the next element in S until we reach the end of the list.

    >>> s = [3, 2, 1]
    >>> foldl(s, sub, 0)      # sub(sub(sub(0, 3), 2), 1)
    -6
    >>> foldl(s, add, 0)      # add(add(add(0, 3), 2), 1)
    6
    >>> foldl(s, mul, 1)      # mul(mul(mul(1, 3), 2), 1)
    6

    >>> foldl([], sub, 100)   # return start if s is empty
    100
    """
    "*** YOUR CODE HERE ***"
    for i in s:
        start = f(start, i)
    return start

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function CONDITION.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def f(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return f

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    # 对比标准答案，这个方法在函数调用时是一级一级调用，如果n的数值过大则可能出现堆栈溢出
    # 标准答案是每次计算上一个的返回值，不用维护函数调用栈，减少了开销
    fs = [f1, f2, f3]

    def gen(f1, f2):
        return lambda x: f1(f2(x))

    def my_cycle(n):
        identity = lambda x: x
        for i in range(n):
            identity = gen(fs[i % len(fs)], identity)
        return identity
    return my_cycle

    # def switch(i):
    #     return [f1, f2, f3][i % 3]
    #
    # def make_cycle(n):
    #     def apply_n_times(x):
    #         for i in range(n):
    #             x = switch(i)(x)
    #         return x
    #     return apply_n_times
    # return make_cycle
