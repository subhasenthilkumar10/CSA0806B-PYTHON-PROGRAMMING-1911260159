"""Modified design for seasonal rates and a ten-day volume bonus."""
from decimal import Decimal, ROUND_HALF_UP

def money(value):
    """Round rupees to two decimal places."""
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def get_rate_card(month):
    """Return the base and step values for the selected month."""
    if month in (4, 5, 6):
        return Decimal("32.00"), Decimal("0.45"), Decimal("0.30")
    return Decimal("30.00"), Decimal("0.40"), Decimal("0.30")

def rate_per_litre(fat, snf, month):
    """Calculate rate from two-decimal analyser readings."""
    base, fat_value, snf_value = get_rate_card(month)
    fat_steps = (Decimal(str(fat)) - Decimal("3.5")) / Decimal("0.1")
    snf_steps = (Decimal(str(snf)) - Decimal("8.5")) / Decimal("0.1")
    return money(base + fat_steps * fat_value + snf_steps * snf_value)

def ten_day_payment(entries, month):
    """Calculate payment and apply the volume bonus when eligible."""
    total_litres = sum((Decimal(str(row["litres"])) for row in entries), Decimal("0"))
    total = sum((money(Decimal(str(row["litres"])) * rate_per_litre(row["fat"], row["snf"], month))
                 for row in entries), Decimal("0.00"))
    bonus = Decimal("0.50") * total_litres if total_litres > 500 else Decimal("0.00")
    return money(total + bonus), money(bonus), total_litres

if __name__ == "__main__":
    sample = [
        {"litres": "300", "fat": "4.25", "snf": "8.65"},
        {"litres": "250.5", "fat": "3.75", "snf": "8.55"},
    ]
    for month in (2, 4):
        total, bonus, litres = ten_day_payment(sample, month)
        print(f"Month {month}: litres={litres}, bonus={bonus}, total payment={total}")
