from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    """Add decimal strings without binary floating-point error."""
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total

def total_paise(items):
    """Convert each amount to integer paise before adding."""
    total = 0
    for amount in items:
        total += int(Decimal(amount) * 100)
    return total

print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print("Paise  :", total_paise(payments), "paise")
print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print("Decimal(float('0.1')):", Decimal(float("0.1")))
