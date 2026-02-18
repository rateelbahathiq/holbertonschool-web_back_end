#!/usr/bin/env python3
"""Module that provides a function that returns a tuple
containing a string and the square of a number."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a number."""
    return (k, float(v ** 2))
