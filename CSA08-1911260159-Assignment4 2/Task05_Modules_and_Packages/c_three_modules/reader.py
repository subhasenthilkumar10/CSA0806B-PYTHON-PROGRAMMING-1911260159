def read_records(path):
    rows = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[2] in ("P", "A"):
                rows.append(parts)
    return rows
