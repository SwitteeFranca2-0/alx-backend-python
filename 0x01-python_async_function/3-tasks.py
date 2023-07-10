#!usr/bin/env python3
"""Tasks in asyncio"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_dalay: int) -> asyncio.Task:
    """Returns an ayncio.Task"""
    task = asyncio.create_task(wait_random(max_dalay))
    return task
