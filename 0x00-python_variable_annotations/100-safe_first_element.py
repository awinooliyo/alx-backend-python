#!/usr/bin/env python3
"""
Module: safe_first_element

Defines a function to safely retrieve the
first element from a list of unknown types.
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
