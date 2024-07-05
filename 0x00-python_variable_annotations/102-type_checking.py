#!/usr/bin/env python3
"""
Module: zoom_array

Provides a function to zoom in on a tuple by duplicating
each element a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on the tuple by duplicating each element a specified
    number of times.

    Args:
        lst (Tuple[int, ...]): The tuple of integers to be zoomed in.
        factor (int, optional): The zoom factor, i.e., how many times
        to duplicate each element. Defaults to 2.

    Returns:
        Tuple[int, ...]: The zoomed-in tuple where each
        element is duplicated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)
