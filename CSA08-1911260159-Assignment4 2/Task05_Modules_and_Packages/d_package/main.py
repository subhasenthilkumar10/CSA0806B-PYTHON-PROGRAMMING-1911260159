from pathlib import Path
from attendance import reader, stats, report

if __name__ == "__main__":
    here = Path(__file__).parent
    rows = reader.read_records(here / "attendance.csv")
    values = stats.percentage(rows)
    report.write_report(values, here / "percentage_report.txt")
    print("Percentages:", values)
    print("Absent on 3+ days:", stats.absent_three_days(rows))
