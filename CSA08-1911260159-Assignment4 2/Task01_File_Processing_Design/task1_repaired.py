from pathlib import Path

def total_mess_bill(file_name):
    total = 0.0
    report_lines = []
    rejected_lines = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                try:
                    if len(parts) != 3:
                        raise ValueError("expected register number, name and amount")
                    name = parts[1].strip()
                    amount = float(parts[2].strip())
                    total += amount
                    report_lines.append(f"{name} - Rs.{amount:.2f}")
                except ValueError as error:
                    rejected_lines.append((line_number, line, str(error)))

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print("MESS BILL REPORT")
    for item in report_lines:
        print(item)
    print(f"Total: Rs.{total:.2f}")

    print("\\nRejected lines:")
    for item in rejected_lines:
        print(item)

if __name__ == "__main__":
    total_mess_bill(Path(__file__).with_name("mess_oct.txt"))
