#!/usr/bin/env python3
"""
Module: sum_list

This module contains a function to compute the sum of a list of floats.

Functions:
    sum_list(input_list: List[float]) -> float:
        Computes the sum of the input list of floats
        and returns it as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats and returns the result.

    Args:
        input_list (List[float]): The list of floats
        for which to compute the sum.

    Returns:
        float: The sum of the input list of floats.
    """
    return sum(input_list)
