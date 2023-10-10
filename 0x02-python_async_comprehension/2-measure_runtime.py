#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather
    measure the total runtime and return it
    """
    start = time.time()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end = time.time()
    runtime = end - start
    return runtime
