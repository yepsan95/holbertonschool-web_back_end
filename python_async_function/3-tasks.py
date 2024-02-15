#!/usr/bin/env python3
"""Defines a function task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates a task with the function wait_random and returns it
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
