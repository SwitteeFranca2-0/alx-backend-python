#!/usr/bin/env python3
"""Make multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """creates a multiplier"""
    return lambda x: x * multiplier
