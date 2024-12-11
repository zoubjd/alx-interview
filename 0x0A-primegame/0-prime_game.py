#!/usr/bin/python3
"""prime game"""
from typing import List


def isPrime(n):
    """checks if a num is prime"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def primeList(num):
    """returns a list of prime numbers"""
    return [i for i in range(2, num + 1) if isPrime(i)]


def isWinner(x: int, nums: List[int]) -> str:
    """determines the winner"""
    if x <= 0 or len(nums) == 0 or x > len(nums):
        return None

    maria = 0
    ben = 0

    for rounds in range(x):
        primes = primeList(nums[rounds])
        if len(primes) % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    else:
        return None
