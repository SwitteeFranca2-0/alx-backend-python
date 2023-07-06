#!/usr/bin/env python3
"""Safe first element"""
from typing import Union, Sequence, Any, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
