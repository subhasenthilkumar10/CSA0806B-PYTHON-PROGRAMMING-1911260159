class InvalidRegistration(Exception):
    """Raised when a registration row is incomplete or invalid."""

def validate_line(line):
    parts = [part.strip() for part in line.strip().split(",")]
    if len(parts) != 5:
        raise InvalidRegistration(f"expected 5 fields, found {len(parts)}")

    reg_no, name, department, email, event_text = parts
    if not reg_no or not name or not department or not event_text:
        raise InvalidRegistration("one or more required fields are empty")

    # Simple email check using string methods, suitable for this assignment.
    if "@" not in email or "." not in email.split("@")[-1] or email.startswith("@"):
        raise InvalidRegistration(f"invalid email {email!r}")

    events = [event.strip() for event in event_text.split(";") if event.strip()]
    if not events:
        raise InvalidRegistration("no events selected")
    return {
        "reg_no": reg_no,
        "name": name,
        "department": department,
        "email": email,
        "events": events
    }
