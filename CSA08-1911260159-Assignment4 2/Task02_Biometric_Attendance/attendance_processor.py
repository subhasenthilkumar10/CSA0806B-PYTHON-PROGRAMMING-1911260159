from pathlib import Path

def process_month(folder_name, output_folder):
    folder = Path(folder_name)
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)

    counts = {}       # register number: [present, absent]
    rejected = []

    for file_path in sorted(folder.glob("*.txt")):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    parts = line.strip().split(",")
                    try:
                        if len(parts) != 3:
                            raise ValueError("expected 3 fields")
                        reg_no, date, status = [part.strip() for part in parts]
                        if status not in ("P", "A"):
                            raise ValueError(f"invalid status {status!r}")
                        if reg_no not in counts:
                            counts[reg_no] = [0, 0]
                        if status == "P":
                            counts[reg_no][0] += 1
                        else:
                            counts[reg_no][1] += 1
                    except ValueError as error:
                        rejected.append(
                            f"{file_path.name},{line_number},{line.strip()},{error}"
                        )
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
            rejected.append(f"{file_path.name},0,FILE ERROR,{error}")

    low_attendance = []
    summary_lines = ["Register Number,Present,Absent,Percentage"]
    for reg_no, values in sorted(counts.items()):
        present, absent = values
        total = present + absent
        percentage = present / total * 100 if total else 0
        summary_lines.append(f"{reg_no},{present},{absent},{percentage:.2f}")
        if percentage < 75:
            low_attendance.append(f"{reg_no},{percentage:.2f}")

    (output / "monthly_summary.csv").write_text(
        "\n".join(summary_lines) + "\n", encoding="utf-8"
    )
    (output / "below_75_percent.csv").write_text(
        "Register Number,Percentage\n" + "\n".join(low_attendance) + "\n",
        encoding="utf-8"
    )
    (output / "damaged_lines.log").write_text(
        "\n".join(rejected) + ("\n" if rejected else ""), encoding="utf-8"
    )

    print("MONTHLY SUMMARY")
    print("\n".join(summary_lines))
    print("\nBelow 75%:", low_attendance)
    print("Damaged lines:", len(rejected))

if __name__ == "__main__":
    here = Path(__file__).parent
    process_month(here / "input", here / "output")
