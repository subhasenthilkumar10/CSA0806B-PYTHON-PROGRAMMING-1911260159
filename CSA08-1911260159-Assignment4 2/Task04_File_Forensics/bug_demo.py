from pathlib import Path

ROOT = Path(__file__).parent
LOG = ROOT / "buggy_returns.log"

def save_returns(books):
    log = open(LOG, "w", encoding="utf-8")
    for book in books:
        log.write(book)
    log.close()

def process(day_file):
    try:
        books = open(day_file, encoding="utf-8").read().split("\n")
        save_returns(books)
    except FileNotFoundError:
        print("missing")

if __name__ == "__main__":
    for day in ("day1.txt", "day2.txt", "day3.txt"):
        process(ROOT / "input" / day)
    print("Buggy log contents:")
    print(repr(LOG.read_text(encoding="utf-8")))
