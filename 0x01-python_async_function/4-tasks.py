#!/usr/bin/env python3
"""
multiple coroutines at the same time with async
"""
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """
    return the list of all the delays
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    complete = asyncio.as_completed(task)
    sorted_list = [await tasks for tasks in complete]

    return sorted_list
