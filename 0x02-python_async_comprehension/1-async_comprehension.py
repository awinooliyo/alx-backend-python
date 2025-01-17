#!/usr/bin/env python3
"""
A coroutine, async_comprehension, that takes no arguments,
collects 10 random numbers using an async comprehensing over
async_generator, then returns the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns the 10 random numbers"""
    outcomes = [i async for i in async_generator()]
    return outcomes
