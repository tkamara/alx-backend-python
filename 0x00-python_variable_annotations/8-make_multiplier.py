#!/usr/bin/env python3
"""
type-annotated function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float as arg and
    returns a function that multiplies a float by multiplier
    """
    def mult_func(f: float) -> float:
        """the function to be returned"""
        return f * multiplier

    return mult_func
