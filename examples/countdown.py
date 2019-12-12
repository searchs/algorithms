import time


def countdown(n):
    if n == 0:
        print(n)
        return 0
    else:
        print(n)
        time.sleep(1)
        return countdown(n -1)


def iter_countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)


b = 5
# iter_countdown(5)

c = 0
# iter_countdown(c)

# countdown(b)
# print("Base condition")
# countdown(c)


def least_missing(alist):
    if len(alist) < 2:
        return alist[0] + 1
    else:
        n = min(alist)
        if n <= 0:
            return 1
        while n in alist:
            n += 1
            continue
    return n


"""Recursive with Lambda: E.g Factorial
f = lambda x: 1 if x in (1,2) else f(x-1)+f(x-2)
"""


def recur_least_missing(alist):
    if min(alist) <= 0:
        return 1
    if len(alist) <2:
        return alist[0] + 1
    else:
        n = min(alist)
        while n in alist:
            n += 1
            continue
    return n

'''
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.'''

assert recur_least_missing([1, 3, 6, 4, 1, 2]) == 5, "ERROR: Should return 5"
print(recur_least_missing([2,3,-4]))
print(recur_least_missing([2,3,5,6,0,4,8]))
print(recur_least_missing([2,3,4,5,6,8]))
mx = list(range(-1000, 1000))
print(recur_least_missing(mx))
# print(mx[:23])
