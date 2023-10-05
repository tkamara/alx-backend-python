#!/usr/bin/env python3
"""
augmenting code with correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    augmenting code with correct duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
