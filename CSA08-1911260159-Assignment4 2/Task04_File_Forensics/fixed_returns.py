from pathlib import Path

ROOT = Path(__file__).parent
LOG = ROOT / "returns.log"
ERROR_LOG = ROOT / "errors.log"

def save_returns(books):
    with open(LOG, "a", encoding="utf-8") as log:
        for book in books:
            if book.strip():
                log.write(book.strip() + "\n")

def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = file.read().splitlines()
        save_returns(books)
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        with open(ERROR_LOG, "a", encoding="utf-8") as error_file:
            error_file.write(f"{day_file}: {error}\n")
        print(f"Could not process {day_file}: {error}")

if __name__ == "__main__":
    for day in ("day1.txt", "day2.txt", "day3.txt", "missing_day.txt"):
        process(ROOT / "input" / day)
    print("Fixed log:")
    print(LOG.read_text(encoding="utf-8"))
    print("Error log:")
    print(ERROR_LOG.read_text(encoding="utf-8"))
