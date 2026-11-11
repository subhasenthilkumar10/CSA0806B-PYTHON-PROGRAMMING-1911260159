from pathlib import Path

def read_records(path):
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[2] in ("P", "A"):
                records.append(parts)
    return records

def percentage(records):
    totals = {}
    for reg_no, date, status in records:
        totals.setdefault(reg_no, [0, 0])
        totals[reg_no][0 if status == "P" else 1] += 1
    return {reg: round(values[0] / sum(values) * 100, 2)
            for reg, values in totals.items() if sum(values)}

def absent_three_days(rows):
    from datetime import date, timedelta

    absent = {}
    for reg, day_text, status in rows:
        if status == "A":
            try:
                day = date.fromisoformat(day_text)
                absent.setdefault(reg, set()).add(day)
            except ValueError:
                continue

    result = []
    for reg, days in absent.items():
        for day in days:
            if (day + timedelta(days=1) in days and
                    day + timedelta(days=2) in days):
                result.append(reg)
                break
    return result
def write_report(values, path):
    with open(path, "w", encoding="utf-8") as file:
        for reg, value in values.items():
            file.write(f"{reg},{value}%\\n")

if __name__ == "__main__":
    here = Path(__file__).parent
    rows = read_records(here / "attendance.csv")
    result = percentage(rows)
    write_report(result, here / "percentage_report.txt")
    print("Percentages:", result)
    print("Absent on 3+ days:", absent_three_days(rows))
