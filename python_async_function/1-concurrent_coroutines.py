#!/usr/bin/env python3
"""Defines async routine called wait_n.
You will spawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that returns the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency.
    """
    delays = []
    all_delays = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
