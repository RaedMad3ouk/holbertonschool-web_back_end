#!/usr/bin/env python3
"""Async Comprehension"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """using an async comprehensing over async_generator"""

    return [n async for n in async_generator()]
    """async for i in async_generator():
        result.append(i)"""
    return result
