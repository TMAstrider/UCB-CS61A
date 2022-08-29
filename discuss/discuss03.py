
# Q1.1 #

def multiply(m, n) :
    if n == 1 :
        return m
    return m + multiply(m, n-1)

print(multiply(100, 10))

# 1.3 #

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)

hailstone(10)
# def hailstoneself():
#     print(n)
#     if n == 1 :   
#         return 1          ## the thing is print out the sequence, and the return values do not matter. ##
#     elif n % 2 == 0:
#         return 

# Q1.4 #
def recursive_is_prime(n) :
    def gra_prime(index) :
        if index == n :
            return True
        elif n % index == 0 or n == 1 :
            return False
        else :
            return gra_prime(index + 1)
    return gra_prime(2)

def is_prime(n) :

    def prime_helper(index):
        if index == n:
            return True
        elif n % index == 0 or n == 1:
            return False
        else:
            return prime_helper(index + 1)
    return prime_helper(2)

print(is_prime(7))

# Q 1.5 merge #
def merge(n1, n2):
    '''merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    '''
    if n1 == 0:
        return n2
    elif n2 == 0 :
        return n1
    elif n1 % 10 < n2 % 10 :
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else :
        return merge(n1, n2 // 10) * 10 + n2 % 10

