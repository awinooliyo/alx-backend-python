#!/usr/bin/env python3
"""
Module: floor

This module contains a function to compute the floor of a float number.

Functions:
    floor(n: float) -> int:
        Computes the floor of the input float number and returns
        it as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Computes the floor of a float number and returns it.

    Args:
        n (float): The float number for which to compute the floor.

    Returns:
        int: The floor of the input float number as an integer.
    """
    return math.floor(n)
