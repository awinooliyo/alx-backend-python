#!/usr/bin/env python3
"""
A coroutine async_generator that takes no arguments,
loops ten times, each time asynchronously wait 1 second,
the yields a random number between 0 and 10.
"""


import asyncio
import random
from typing import Generator


async def async_generator():
    """Loops 10 times, wait 1 sec each time"""
    for y in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
