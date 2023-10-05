#!/usr/bin/env python3
"""type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list input_list of floats as arg and returns their sum as a float
    """
    ans = 0.0
    for num in input_list:
        ans += num

    return ans
