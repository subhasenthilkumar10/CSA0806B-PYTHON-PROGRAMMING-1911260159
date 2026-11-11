import os
import tempfile

class InvalidRecord(Exception):
    """Raised when a line is not in the expected attendance format."""

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    reg_no, date, status = [part.strip() for part in parts]
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status {status!r}")
    return reg_no, date, status

def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    if not line.strip():
                        continue
                    reg_no, date, status = parse_line(line)
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as error:
                    errors.append((line_number, str(error)))
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Attendance file not found: {path}") from error
    except PermissionError as error:
        raise PermissionError(f"Cannot read attendance file: {path}") from error
    except UnicodeDecodeError as error:
        raise ValueError(f"File is not valid UTF-8: {path}") from error
    else:
        print(f"Successfully processed: {path}")
    finally:
        print("File processing attempt finished.")

    return present, absent, errors

data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                 encoding="utf-8") as tmp:
    tmp.write(data)
    file_name = tmp.name

try:
    print(summarise(file_name))
finally:
    os.remove(file_name)

print("\nMissing-file test:")
try:
    summarise("file_that_does_not_exist.csv")
except FileNotFoundError as error:
    print(error)
