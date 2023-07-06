#!/usr/bin/env python3
"""sum of mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the sum of a list with mixed data type"""
    return sum(mxd_list)
