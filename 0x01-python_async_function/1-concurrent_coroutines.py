#!/usr/bin/env python3
"""
multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays
    """
    task = [wait_random(max_delay) for _ in range(n)]
    complete = asyncio.as_completed(task)
    sorted_list = [await tasks for tasks in complete]

    return sorted_list
