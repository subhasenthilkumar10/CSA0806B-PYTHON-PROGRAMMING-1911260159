def read_records(path):
    rows = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[2] in ("P", "A"):
                rows.append(parts)
    return rows

def percentage(rows):
    totals = {}
    for reg, date, status in rows:
        totals.setdefault(reg, [0, 0])
        totals[reg][0 if status == "P" else 1] += 1
    return {reg: round(v[0] / sum(v) * 100, 2)
            for reg, v in totals.items() if sum(v)}

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
            file.write(f"{reg},{value}%\n")
