"""Command-line calculator for a small collection of farmer entries."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from decimal import Decimal
from Task07_Modules.milkrate import validate_entry, payout, ten_day_total

def main():
    """Run a sample collection and show the ten-day payment."""
    entries = [
        {"farmer_id": "F101", "litres": "10", "fat": "3.5", "snf": "8.5", "shift": "MORNING"},
        {"farmer_id": "F101", "litres": "8.5", "fat": "4.2", "snf": "8.7", "shift": "EVENING"},
        {"farmer_id": "F101", "litres": "12", "fat": "3.1", "snf": "8.3", "shift": "MORNING"},
        {"farmer_id": "F102", "litres": "5", "fat": "2.0", "snf": "8.5", "shift": "EVENING"},
        {"farmer_id": "F102", "litres": "6", "fat": "7.0", "snf": "8.5", "shift": "MORNING"},
    ]
    for item in entries:
        validate_entry(item["farmer_id"], item["litres"], item["fat"], item["snf"], item["shift"])
        item["amount"] = payout(item["litres"], item["fat"], item["snf"])
        print(f'{item["farmer_id"]:5} {item["litres"]:>6} L  {item["amount"]:>8.2f}')
    print("Total of five entries:", sum((item["amount"] for item in entries), Decimal("0.00")))

if __name__ == "__main__":
    main()
