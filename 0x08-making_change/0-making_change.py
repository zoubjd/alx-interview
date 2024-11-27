#!/usr/bin/python3
"""coin change problem"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """returns the fewest number of coins needed to meet a given amount"""
    if total <= 0:
        return 0
    cointotal = 0
    coins = sorted(coins, reverse=True)
    n = len(coins)
    for coin in coins:
        if total == 0:
            return cointotal
        while total >= coin:
            total = total - coin
            cointotal += 1
    if total > 0:
        return -1
    return cointotal
