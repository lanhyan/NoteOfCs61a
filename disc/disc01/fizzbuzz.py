def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    a = 1
    while a <= n:
        if a % 3 == 0 and a % 5 == 0:
            print('fizzbuzz')
        elif a % 3 == 0:
            print('fizz')
        elif a % 5 == 0:
            print('buzz')
        else:
            print(a)
        a += 1
