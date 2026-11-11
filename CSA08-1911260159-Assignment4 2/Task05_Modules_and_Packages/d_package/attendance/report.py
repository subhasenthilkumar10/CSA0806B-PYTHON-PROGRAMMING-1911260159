def write_report(values, path):
    with open(path, "w", encoding="utf-8") as file:
        for reg, value in values.items():
            file.write(f"{reg},{value}%\\n")
