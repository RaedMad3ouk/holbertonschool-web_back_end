#!/usr/bin/env python3
"""a type-annotated function"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
    and returns a tuple"""
    return (k, v * v)
