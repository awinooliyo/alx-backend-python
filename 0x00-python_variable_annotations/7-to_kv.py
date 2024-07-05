#!/usr/bin/env python3
"""
Module: to_kv

This module contains a function to create a tuple where the first element is a
string and the second element is the square of an int or float.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Takes a string k and an int OR float v as arguments and returns a tuple
        containing k and the square of v as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple where the first element is a string k and the second element
    is the square of an int or float v.

    Args:
        k (str): The string element of the tuple.
        v (Union[int, float]): The int or float element of the tuple.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v ** 2))
