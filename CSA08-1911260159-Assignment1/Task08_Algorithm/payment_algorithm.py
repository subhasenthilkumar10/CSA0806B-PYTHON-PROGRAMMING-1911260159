"""Store entries and calculate the ten-day total."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from decimal import Decimal
from Task07_Modules.milkrate import validate_entry, payout, ten_day_total

entries = [
    {"farmer_id": "F101", "litres": "10", "fat": "3.5", "snf": "8.5", "shift": "MORNING"},
    {"farmer_id": "F101", "litres": "8.5", "fat": "4.2", "snf": "8.7", "shift": "EVENING"},
    {"farmer_id": "F101", "litres": "12", "fat": "3.1", "snf": "8.3", "shift": "MORNING"},
]

payments = []
for entry in entries:
    validate_entry(entry["farmer_id"], entry["litres"], entry["fat"], entry["snf"], entry["shift"])
    amount = payout(entry["litres"], entry["fat"], entry["snf"])
    payments.append(amount)
    print(entry["farmer_id"], "payment =", amount)

print("Ten-day total =", ten_day_total(entries))
