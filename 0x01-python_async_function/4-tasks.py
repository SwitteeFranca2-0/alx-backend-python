#!/usr/bin/env python3
"""Taks on asyncio"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """Run a concurrent function with it"""
    vals = [task_wait_random(max_delay) for i in range(0, n)]
    val = await asyncio.gather(*vals)
    return sorted(val)
