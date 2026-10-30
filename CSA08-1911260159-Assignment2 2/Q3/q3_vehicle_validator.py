# Q3 - Vehicle registration number validator
# Uses string methods and slicing only; no regular expressions.


def normalise(text):
    """Remove spaces and hyphens, then convert to uppercase."""
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Valid: 2 letters, 2 digits, 1 or 2 letters, 4 digits."""
    if len(reg) not in (9, 10):
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    number = reg[-4:]

    return (state.isalpha() and state.isupper()
            and district.isdigit()
            and len(series) in (1, 2)
            and series.isalpha() and series.isupper()
            and number.isdigit())


def format_receipt(reg):
    if not is_valid(reg):
        return "INVALID"
    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


samples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "Tn09Ab1234",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 C 4567"
]

print("Q3 - VEHICLE NUMBER VALIDATION")
for raw in samples:
    reg = normalise(raw)
    status = "valid" if is_valid(reg) else "INVALID"
    print(f"{raw:15} -> {reg:11} {status}")

print("\nReceipt format:", format_receipt(normalise("tn 09 ab 1234")))
