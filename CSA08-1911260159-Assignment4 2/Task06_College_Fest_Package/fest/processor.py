def remove_duplicates(registrations, errors):
    clean = []
    seen_register_numbers = set()
    for item in registrations:
        reg_no = item["reg_no"]
        if reg_no in seen_register_numbers:
            errors.append(f"DUPLICATE,{reg_no},duplicate registration ignored")
        else:
            seen_register_numbers.add(reg_no)
            clean.append(item)
    return clean

def make_event_lists(registrations):
    event_lists = {}
    for item in registrations:
        for event in item["events"]:
            event_lists.setdefault(event, []).append(item)
    return event_lists
