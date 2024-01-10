#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return sum of list element"""
    sum: float = 0
    x: int = 0
    for x in range(len(input_list)):
        sum = sum + input_list[x]
    return sum
