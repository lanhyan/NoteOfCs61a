def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

@memoize
def fib(n):
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)
