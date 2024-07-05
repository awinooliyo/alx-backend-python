#!/usr/bin/env python3
"""
Module: concat

This module contains a function to concatenate two strings.

Functions:
    concat(str1: str, str2: str) -> str:
        Concatenates two input strings and returns the result as a new string.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenated string of str1 followed by str2.
    """
    return str1 + str2
