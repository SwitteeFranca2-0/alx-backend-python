#!/usr/bin/env python3
"""Safe first element"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns teh first element of an iterable"""
    if lst:
        return lst[0]
    else:
        return None
