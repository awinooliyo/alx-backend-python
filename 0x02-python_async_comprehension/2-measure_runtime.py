#!/usr/bin/env python3
"""
Execute async_comprehension four times in parallel
and measure the total runtime.
The coroutine will create four async tasks using
async_comprehension and run them in parallel
using asyncio.gather.
It will measure the total time taken to execute these tasks.
Returns, float: The total runtime in seconds.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime"""
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()
    return end_time - start_time
