# Q4 - Building long text using + and join
import time


def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text


def build_join(parts):
    return ";".join(parts) + ";"


def build_fstring(parts):
    lines = [f"{part};" for part in parts]
    return "".join(lines)


def measure(function, parts, repeats=3):
    times = []
    result = ""
    for _ in range(repeats):
        start = time.perf_counter()
        result = function(parts)
        times.append(time.perf_counter() - start)
    return result, times, sum(times) / len(times)


if __name__ == "__main__":
    print("Q4 - STRING BUILDING TIMINGS (seconds)")
    for size in (1000, 10000, 200000):
        items = [f"Item{i}:Rs{i % 50}" for i in range(size)]
        plus_text, plus_times, plus_avg = measure(build_plus, items)
        join_text, join_times, join_avg = measure(build_join, items)
        f_text, f_times, f_avg = measure(build_fstring, items)

        print(f"\nItems: {size}")
        print("Same result:", plus_text == join_text == f_text)
        print("Plus times:", [round(x, 4) for x in plus_times],
              "average:", round(plus_avg, 4))
        print("Join times:", [round(x, 4) for x in join_times],
              "average:", round(join_avg, 4))
        print("F-string times:", [round(x, 4) for x in f_times],
              "average:", round(f_avg, 4))

    print("\nOriginal assignment size check:")
    items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]
    a = build_plus(items)
    b = build_join(items)
    print("same text:", a == b, "| length:", len(b))
