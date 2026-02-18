#!/usr/bin/env python3
"""Module that provides a function that returns a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    
    def multiply(x: float) -> float:
        """Multiply x by the captured multiplier."""
        return x * multiplier

    return multiply
