from pathlib import Path
from .validator import validate_line, InvalidRegistration

def read_department_files(input_folder, department_files):
    registrations = []
    errors = []
    for file_name in department_files:
        path = Path(input_folder) / file_name
        try:
            with open(path, "r", encoding="utf-8") as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    try:
                        registrations.append(validate_line(line))
                    except InvalidRegistration as error:
                        errors.append(f"{file_name},{line_number},{line.strip()},{error}")
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
            errors.append(f"{file_name},0,FILE ERROR,{error}")
    return registrations, errors
