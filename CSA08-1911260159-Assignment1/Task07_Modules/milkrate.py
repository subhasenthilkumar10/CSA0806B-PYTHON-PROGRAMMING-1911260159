"""Simple rate card and payment calculations for Ksheera co-operative."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

def money(value):
    """Round a rupee value to the nearest paisa."""
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Return the milk rate using the original rate card."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return money(rate)

def payout(litres, fat, snf):
    """Return the payment for one milk entry."""
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf))

def validate_entry(farmer_id, litres, fat, snf, shift):
    """Check the values entered for one collection."""
    if not farmer_id.strip():
        raise ValueError("Farmer ID cannot be empty")
    litres = Decimal(str(litres))
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    if not (MIN_FAT <= fat <= MAX_FAT):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if not (Decimal("0") <= snf <= Decimal("15")):
        raise ValueError("SNF must be between 0 and 15")
    if shift.upper() not in ("MORNING", "EVENING"):
        raise ValueError("Shift must be MORNING or EVENING")
    return True

def ten_day_total(entries):
    """Add already-rounded payments for a farmer's ten-day period."""
    total = Decimal("0.00")
    for entry in entries:
        total += payout(entry["litres"], entry["fat"], entry["snf"])
    return money(total)

if __name__ == "__main__":
    samples = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    for litres, fat, snf in samples:
        rate = rate_per_litre(fat, snf)
        print(f"{litres:5} L  fat {fat:4}  snf {snf:4}  rate {rate:6.2f}  pay {payout(litres, fat, snf):8.2f}")
