def is_prime(n):
    if n == 1:
        return False
    c = 2
    while c < n:
        if n % c == 0:
            return False
        c += 1
    return True
