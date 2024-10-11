#!/usr/bin/python3
"""lockboxes
the first box is always unlocked"""


def canUnlockAll(boxes):
    """canUnlockAll"""
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    seen_numbers = [False] * len(boxes)  # List of boolean values
    seen_numbers[0] = True

    keys = boxes[0]  # Start with the keys in the first box

    while keys:

        key = keys.pop()

        if key < len(boxes) and not seen_numbers[key]:
            seen_numbers[key] = True  # Mark this box as seen

            keys.extend(boxes[key])
    return all(seen_numbers)
