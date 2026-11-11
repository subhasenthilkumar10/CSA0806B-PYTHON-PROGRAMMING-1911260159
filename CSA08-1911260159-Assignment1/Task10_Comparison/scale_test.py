"""Compare float and Decimal totals at three data sizes."""
from decimal import Decimal
from time import perf_counter

for count in (300, 6000, 150000):
    values = ["33.40"] * count
    start = perf_counter()
    float_total = sum(float(value) for value in values)
    float_time = perf_counter() - start

    start = perf_counter()
    decimal_total = sum((Decimal(value) for value in values), Decimal("0.00"))
    decimal_time = perf_counter() - start

    print(f"{count:>7} payments | float={float_total:.8f} | Decimal={decimal_total:.2f}")
    print(f"          float time={float_time:.6f}s | Decimal time={decimal_time:.6f}s")
