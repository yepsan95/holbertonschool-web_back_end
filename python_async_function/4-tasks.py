#!/usr/bin/env python3
"""Defines task_await_n based on wait_n. The code is nearly
identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that returns the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    delays = []
    all_delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
