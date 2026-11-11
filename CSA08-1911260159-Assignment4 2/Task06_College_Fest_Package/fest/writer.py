from pathlib import Path

def write_outputs(registrations, event_lists, errors, output_folder):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)

    with open(output / "master_list.csv", "w", encoding="utf-8") as file:
        file.write("Register Number,Name,Department,Email,Events\n")
        for item in registrations:
            file.write(
                f'{item["reg_no"]},{item["name"]},{item["department"]},'
                f'{item["email"]},{";".join(item["events"])}\n'
            )

    for event, people in event_lists.items():
        safe_name = "".join(ch.lower() if ch.isalnum() else "_" for ch in event)
        with open(output / f"{safe_name}_participants.txt", "w", encoding="utf-8") as file:
            for person in people:
                file.write(f'{person["reg_no"]},{person["name"]},{person["department"]}\n')

    with open(output / "summary_report.txt", "w", encoding="utf-8") as file:
        file.write(f"Total valid unique registrations: {len(registrations)}\n")
        file.write(f"Events: {len(event_lists)}\n")
        for event, people in sorted(event_lists.items()):
            file.write(f"{event}: {len(people)} participant(s)\n")

    with open(output / "error_log.txt", "w", encoding="utf-8") as file:
        for error in errors:
            file.write(error + "\n")
