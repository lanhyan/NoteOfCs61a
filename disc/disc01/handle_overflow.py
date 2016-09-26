def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow.
    >>> handle_overflow(35, 29)
    1 spots left in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section.
    """
    if s1 >= 30:
        if s2 >= 30:
            print('No space left in either section.')
        else:
            print(str(30 - s2) + ' spots left in Section 2.')
    else:
        if s2 >= 30:
            print(str(30 - s1) + ' spots left in Section 1.')
        else:
            print('No overflow.')
