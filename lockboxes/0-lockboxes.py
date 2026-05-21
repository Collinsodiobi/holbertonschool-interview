#!/usr/bin/python3
"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened.
    """
    n = len(boxes)
    opened = set()
    stack = [0]  # start with box 0

    while stack:
        box = stack.pop()

        if box in opened:
            continue

        if box < 0 or box >= n:
            continue

        opened.add(box)

        for key in boxes[box]:
            if key not in opened:
                stack.append(key)

    return len(opened) == n
