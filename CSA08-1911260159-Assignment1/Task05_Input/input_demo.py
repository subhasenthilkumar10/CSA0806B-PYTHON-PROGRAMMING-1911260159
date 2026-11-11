"""Read text, convert it and handle invalid entries simply."""
def read_number(prompt):
    while True:
        text = input(prompt).strip()
        try:
            return float(text)
        except ValueError:
            print("Please enter a number, for example 8.5.")

litres = read_number("Enter litres: ")
fat = read_number("Enter fat percentage: ")
print(f"Accepted: {litres:.2f} litres, fat {fat:.2f}%")
