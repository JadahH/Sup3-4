import argparse
import multiprocessing
import sys
import time
import unittest


def if_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def range_split(start: int, end: int, chunks: int) -> list[tuple[int, int]]:
    total = end - start + 1
    base, extra = divmod(total, chunks)
    ranges = []
    cur = start
    for i in range(chunks):
        size = base + (1 if i < extra else 0)
        sub_start = cur
        sub_end = cur + size - 1
        ranges.append((sub_start, sub_end))
        cur = sub_end + 1
    return ranges