#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ executes comprehension func 4 times in parallel, returns runtime """

    t0 = time.time()
    fcts = [async_comprehension() for i in range(4)]
    await asyncio.gather(*fcts)

    return time.time() - t0
