#!/usr/bin/env python3
"""measuring the runtime"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n
    """
    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    ans = total_time / n

    return ans
