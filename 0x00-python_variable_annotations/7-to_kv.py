#!/usr/bin/env python3
"""A function that takes in data of various types"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes two arguments to return a tuple"""
    return (k, v**2)
