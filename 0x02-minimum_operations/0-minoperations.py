#!/usr/bin/python3
"""trying to get to n using the best route"""
import typing


def is_prime(num) -> bool:
    """finds if a num is prime"""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def findprimefactors(n: int) -> typing.List[int]:
    """returns all the prime factors, including duplicates"""
    primelist = []
    factor = 2
    while factor <= n:
        if n % factor == 0 and is_prime(factor):
            while n % factor == 0:
                primelist.append(factor)
                n //= factor
        factor += 1
    return primelist


def minOperations(n: int) -> int:
    """minimum operation"""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    if is_prime(n):
        return n

    primelist = findprimefactors(n)
    if not primelist:
        return 0

    return sum(primelist)
