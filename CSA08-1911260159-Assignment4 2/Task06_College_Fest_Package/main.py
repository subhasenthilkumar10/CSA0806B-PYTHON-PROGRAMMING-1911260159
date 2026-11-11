from pathlib import Path
from fest.reader import read_department_files
from fest.processor import remove_duplicates, make_event_lists
from fest.writer import write_outputs

if __name__ == "__main__":
    here = Path(__file__).parent
    department_files = [
        "department_cse.txt",
        "department_eee.txt",
        "department_mech.txt",  # intentionally missing for testing
    ]

    registrations, errors = read_department_files(
        here / "input", department_files
    )
    clean = remove_duplicates(registrations, errors)
    event_lists = make_event_lists(clean)
    write_outputs(clean, event_lists, errors, here / "output")

    print("Valid unique registrations:", len(clean))
    print("Events created:", sorted(event_lists))
    print("Errors recorded:", len(errors))
    print("Check the output folder for all reports.")
