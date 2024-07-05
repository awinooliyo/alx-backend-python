#!/usr/bin/env python3
"""
Module: make_multiplier

This module contains a function to create a multiplier function based on a
given float multiplier.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Takes a float multiplier as argument and returns a function that
        multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that multiplies a float by the given
    multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that accepts a float and returns
        the result of multiplying that float by the given multiplier.
    """
    def multiplier_function(num: float) -> float:
        return num * multiplier

    return multiplier_function
