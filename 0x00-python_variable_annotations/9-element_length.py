#!/usr/bin/env python3
"""Elemnt length function"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return elements length"""
    return [(i, len(i)) for i in lst]
