"""Assert-based checks for normal and invalid entries."""
import sys
from decimal import Decimal
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Task07_Modules.milkrate import rate_per_litre, payout, validate_entry

assert rate_per_litre(3.5, 8.5) == Decimal("30.00")
assert payout(10, 3.5, 8.5) == Decimal("300.00")
assert rate_per_litre(4.2, 8.7) == Decimal("33.40")
assert rate_per_litre(3.1, 8.3) == Decimal("27.80")
assert rate_per_litre(2.0, 8.5) == Decimal("24.00")
assert rate_per_litre(7.0, 8.5) == Decimal("44.00")

for bad in [
    ("F1", -1, 3.5, 8.5, "MORNING"),
    ("F1", 1, 7.1, 8.5, "MORNING"),
    ("F1", 1, 3.5, 8.5, "NIGHT"),
]:
    try:
        validate_entry(*bad)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid entry was accepted")

print("All valid and invalid-entry tests passed.")
