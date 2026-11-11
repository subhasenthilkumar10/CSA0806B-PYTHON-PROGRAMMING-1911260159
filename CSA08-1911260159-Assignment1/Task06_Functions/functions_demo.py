"""Small functions keep the payment steps easy to test."""
from decimal import Decimal
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Task07_Modules.milkrate import rate_per_litre, payout

def ten_day_total(payments):
    """Return the sum of payment amounts."""
    total = Decimal("0.00")
    for amount in payments:
        total += Decimal(str(amount))
    return total.quantize(Decimal("0.01"))

amounts = [payout(10, 3.5, 8.5), payout(8.5, 4.2, 8.7)]
print("Rate:", rate_per_litre(4.2, 8.7))
print("Ten-day total:", ten_day_total(amounts))
