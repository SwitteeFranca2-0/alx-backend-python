#!/usr/bin/env python3
"""Async comprehensions"""

import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """A function on async comprehension"""
    return [i async for i in async_generator()]