this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder_inc(b):
        c = 0
        nonlocal a
        c = a + b
        a += 1
        return c
    return adder_inc

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    a1 = -1
    a2 = 1
    flag = 1
    def fib():
        nonlocal a1
        nonlocal a2
        nonlocal flag
        ret = 0
        ret = a1 + a2
        if flag == 1:
            a1 = ret
            flag = 0
        else :
            a2 = ret
            flag = 1
        return ret
    return fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    state = 0
    for o in lst:
        if o == entry and state == 0:
            lst.insert(i + 1, elem)
            state = 1
            i += 1
            continue
        state = 0
        i += 1
    return lst
    # flag = 0
    # for i, e in enumerate(lst):
    #     if entry == e and flag == 0:
    #         lst.insert(i+1, elem)
    #         flag = 1
    #         continue
    #     flag = 0
    # return lst

