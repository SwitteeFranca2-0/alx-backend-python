#!/usr/bin/env python3
"""Measure fubtime for async functions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Function that measure the runtim of an async function called 4 times"""
    funcs = [async_comprehension() for i in range(4)]
    begin = time.time()
    await asyncio.gather(*funcs)
    return time.time() - begin
