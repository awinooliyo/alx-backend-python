#!/usr/bin/env python3
"""
Module: sum_mixed_list

This module contains a function to compute the sum of a mixed list of integers
and floats.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Computes the sum of the input mixed list of integers and floats and
        returns it as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Computes the sum of a mixed list of integers and floats and returns the
    result.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list of integers and
        floats for which to compute the sum.

    Returns:
        float: The sum of the input mixed list of integers and floats.
    """
    return sum(mxd_lst)
