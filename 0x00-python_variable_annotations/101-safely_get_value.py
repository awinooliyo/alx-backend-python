#!/usr/bin/env python3
"""
Module: safely_get_value

Provides a function to safely retrieve values
from dictionaries with default fallbacks.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the
    given key from the dictionary.
    If the key is not present, returns the default value.

    Args:
        dct (Mapping): The dictionary-like object to retrieve values from.
        key (Any): The key whose value to retrieve from dct.
        default (Optional[T]): The default value to
            return if key is not in dct. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with key in dct,
        or the default value if key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
