# Q1 - Electricity Subsidy Eligibility
# Separate if statements and if-elif-else comparison

households = [
    ("H1", 100, False, False),
    ("H2", 101, True, False),
    ("H3", 200, True, False),
    ("H4", 201, True, False),
    ("H5", 201, False, True),
    ("H6", 150, False, False),
    ("H7", 80, True, True),
    ("H8", 200, False, True)
]


def separate_if(units, ration_card, senior_member):
    results = []

    if units <= 100:
        results.append("Full subsidy")
    if 101 <= units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and not senior_member:
        results.append("No subsidy")
    if units > 200 and senior_member:
        results.append("Special subsidy")

    if not results:
        results.append("No subsidy")
    return " + ".join(results)


def elif_decision(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        else:
            return "No subsidy"
    else:
        if senior_member:
            return "Special subsidy"
        else:
            return "No subsidy"


print("Q1 - ELECTRICITY SUBSIDY")
print("Household | Separate if | If-elif-else")
for name, units, ration, senior in households:
    first = separate_if(units, ration, senior)
    second = elif_decision(units, ration, senior)
    print(f"{name:9} | {first:20} | {second}")

print("\nBoundary check: 100, 101, 200 and 201 units are included.")
print("Design note: elif makes the main unit ranges mutually exclusive.")
