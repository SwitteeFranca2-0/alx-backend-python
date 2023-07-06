#!/usr/bin/env python3
"""Safe first element"""
from typing import Mapping, Any, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """sfaely get value"""
    if key in dct:
        return dct[key]
    else:
        return default
