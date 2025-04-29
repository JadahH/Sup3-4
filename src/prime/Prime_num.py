import argparse
import multiprocessing
import sys
import time
import unittest

"""
    Determine if a number is prime.

    :param n: Integer to test for primality.
    :return: True if n is a prime number, False otherwise.
"""
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

def subrange(rng: tuple[int, int]) -> list[int]:
    sub_start, sub_end = rng
    return [n for n in range(sub_start, sub_end + 1) if if_prime(n)]

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)

def main():
    parser = argparse.ArgumentParser(description="Find primes in a range using multiprocessing.")
    parser.add_argument('start',   type=int,                        help="Start of range (inclusive)")
    parser.add_argument('end',     type=int,                        help="End of range (inclusive)")
    parser.add_argument('procs',   type=int,                        help="Number of worker processes")
    parser.add_argument('--test',  action='store_true',             help="Run built-in test suite and exit")
    args = parser.parse_args()

    if args.test:
        run_tests()

    if args.start > args.end or args.procs < 1:
        parser.error("Ensure start ≤ end and procs ≥ 1")

    t0 = time.time()

    ranges = range_split(args.start, args.end, args.procs)
    with multiprocessing.Pool(processes=args.procs) as pool:
        results = pool.map(subrange, ranges)

    # flatten and sort
    primes = sorted(p for sublist in results for p in sublist)
    elapsed = time.time() - t0

    print(primes)
    print(f"\nFound {len(primes)} primes in {elapsed:.2f} seconds "
          f"using {args.procs} process{'es' if args.procs>1 else ''}.")

if __name__ == '__main__':
    main()