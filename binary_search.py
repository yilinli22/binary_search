#!/bin/python3


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.
    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if xs == []:
        return None

    def go(left, right):
        if left == right:
            if xs[left] <= 0:
                return None
            else:
                return left
        mid = (left + right) // 2
        if xs[mid] > 0:
            right = mid
        if xs[mid] < 0:
            left = mid + 1
        if xs[mid] == 0:
            left = mid + 1
            return left
        return go(left, right)

    return go(0, len(xs) - 1)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.
    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    if xs == []:
        return 0
    if xs[0] < x:
        return 0
    if xs[-1] > x:
        return 0

    def step_one(xs, x):
        def go(left, right):
            if left == right:
                if xs[left] != x:
                    return right
                else:
                    return left
            mid = (left + right) // 2
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] < x:
                right = mid
            if xs[mid] == x:
                right = mid
            return go(left, right)
        return go(0, len(xs) - 1)

    def step_two(xs, x):
        def goto(left, right):
            if left == right:
                if xs[left] != x:
                    return left
                else:
                    return right + 1
            mid = (left + right) // 2
            if xs[mid] > x:
                left = mid + 1
            if xs[mid] < x:
                right = mid
            if xs[mid] == x:
                left = mid + 1
            return goto(left, right)

        return goto(0, len(xs) - 1)
    return step_two(xs, x) - step_one(xs, x)


def argmin(f, lo, hi, epsilon=1e-3):
    def go(lo, hi):
        m1 = lo + (hi - lo) / 4
        m2 = lo + (hi - lo) / 2
        if hi - lo < epsilon:
            return hi
        if f(m1) > f(m2):
            return go(m1, hi)
        if f(m1) < f(m2):
            return go(lo, m2)
    return go(lo, hi)


###########################################
# the functions below are extra credit
###########################################

def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum
    is guaranteed to be between lo and hi.
    This function is useful for initializing argmin.
    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally
    uses the find_boundaries function so that
    you do not need to specify lo and hi.
    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
