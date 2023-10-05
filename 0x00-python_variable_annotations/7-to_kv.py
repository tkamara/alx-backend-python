#!/usr/bin/env python3
"""type-annotated function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string k and an int OR float v and returns a tuple
    first element of the tuple is the string k
    second element is the square of the int/float v
    """
    return (k, v*v)
