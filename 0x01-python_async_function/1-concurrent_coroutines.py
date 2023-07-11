#!/usr/bin/env python3
"""Running concurrent functions"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run a concurrent function with it"""
    vals = [wait_random(max_delay) for i in range(0, n)]
    val = await asyncio.gather(*vals)
    return sorted(val)
