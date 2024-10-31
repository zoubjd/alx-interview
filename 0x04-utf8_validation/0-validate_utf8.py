#!/usr/bin/python3
"""
uft 8 checking
"""
import typing


def validUTF8(data: typing.List[int]) -> bool:
    """checker func"""
    if not data:
        return False

    for i in data:
        if i > 255 or i < 0:
            return False

    return True
