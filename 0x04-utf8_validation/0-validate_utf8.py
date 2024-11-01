#!/usr/bin/python3
"""
UTF-8 Validation
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    # Number of bytes remaining to complete the current UTF-8 character
    remaining_bytes = 0

    for byte in data:
        # Only consider the last 8 bits of each integer (byte)
        byte &= 0xFF

        if remaining_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1
        else:
            if (byte >> 7) == 0:
                # 1-byte character (0xxxxxxx)
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character (110xxxxx)
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character (1110xxxx)
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character (11110xxx)
                remaining_bytes = 3
            else:
                # Invalid starting byte
                return False

    return remaining_bytes == 0
