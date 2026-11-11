from pathlib import Path
import attendance_utils as attendance

if __name__ == "__main__":
    here = Path(__file__).parent
    rows = attendance.read_records(here / "attendance.csv")
    values = attendance.percentage(rows)
    attendance.write_report(values, here / "percentage_report.txt")
    print("Percentages:", values)
    print("Absent on 3+ days:", attendance.absent_three_days(rows))
