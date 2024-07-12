#!/usr/bin/env python3
"""
A coroutine async_generator that takes no arguments,
loops ten times, each time asynchronously waits 1 second,
then yields a random number between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, waiting 1 second each time and yields
    a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
