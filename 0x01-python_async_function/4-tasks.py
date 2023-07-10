#!/usr/bin/env python3
"""Taks on asyncio python"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run a concurrent function with it"""
    tsks = [task_wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tsks)]
