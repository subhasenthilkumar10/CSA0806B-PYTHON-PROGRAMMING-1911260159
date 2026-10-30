# Q7 - Redesign plain recursive staircase counting
# Original: repeated recursive work.
# Redesigned: iterative solution stores only the previous two answers.

import time

calls = 0


def original_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return original_naive(n - 1) + original_naive(n - 2)


def redesigned_loop(n):
    if n <= 1:
        return 1
    one_step_before = 1
    two_steps_before = 1
    operations = 0

    for _ in range(2, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current
        operations += 1

    return one_step_before, operations


if __name__ == "__main__":
    n = 30

    calls = 0
    start = time.perf_counter()
    old_answer = original_naive(n)
    old_time = time.perf_counter() - start
    old_calls = calls

    start = time.perf_counter()
    new_answer, new_operations = redesigned_loop(n)
    new_time = time.perf_counter() - start

    print("Q7 - ORIGINAL VS REDESIGNED")
    print("Input n:", n)
    print("Original answer:", old_answer)
    print("Original recursive calls:", old_calls)
    print(f"Original time: {old_time:.6f} seconds")
    print("Redesigned answer:", new_answer)
    print("Redesigned loop iterations:", new_operations)
    print(f"Redesigned time: {new_time:.6f} seconds")
    print("Same answer:", old_answer == new_answer)
