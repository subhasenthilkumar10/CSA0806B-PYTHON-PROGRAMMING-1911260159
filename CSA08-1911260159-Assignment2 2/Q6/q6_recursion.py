# Q6 - Counting ways to climb stairs
from functools import lru_cache
import sys
import time

calls = 0


def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    if n <= 1:
        return 1
    previous_two = 1
    previous_one = 1
    for _ in range(2, n + 1):
        current = previous_one + previous_two
        previous_two = previous_one
        previous_one = current
    return previous_one


if __name__ == "__main__":
    print("Q6 - STAIRCASE WAYS")
    for n in range(1, 7):
        print(f"n={n}: {ways_loop(n)} ways")

    for n in (10, 20, 25, 30):
        calls = 0
        naive_answer = ways_naive(n)
        naive_calls = calls

        ways_memo.cache_clear()
        calls = 0
        memo_answer = ways_memo(n)
        memo_calls = calls
        print(f"n={n}: naive={naive_answer}, calls={naive_calls}; "
              f"memo={memo_answer}, calls={memo_calls}")

    print("\nDefault recursion limit:", sys.getrecursionlimit())
    ways_memo.cache_clear()
    try:
        print("Memoised n=1000:", ways_memo(1000))
    except RecursionError:
        print("Memoised n=1000 caused RecursionError at this recursion limit.")

    start = time.perf_counter()
    answer = ways_loop(1000)
    elapsed = time.perf_counter() - start
    print("Loop n=1000 calculated.")
    print("Number of digits:", len(str(answer)))
    print(f"Loop time: {elapsed:.6f} seconds")
