# Q5 - Functions, parameters and scope


def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order


def bill_amount(total, gst_rate=0.05):
    gst = total * gst_rate
    return total, gst


# Local variable example
def show_local():
    message = "I am local to this function"
    print(message)


# Global variable example
college_name = "Engineering College"


def show_global():
    print("Global value:", college_name)


# Nonlocal variable example
def make_counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    return increase


if __name__ == "__main__":
    print("Buggy function:")
    print(add_item_buggy("Tea"), add_item_buggy("Vada"))
    print("Stored default list:", add_item_buggy.__defaults__)

    print("\nCorrect function:")
    print(add_item("Tea"), add_item("Vada"))

    print("\nThree independent customers:")
    customer1 = add_item("Tea")
    customer2 = add_item("Vada")
    customer3 = add_item("Coffee")
    print("Customer 1:", customer1)
    print("Customer 2:", customer2)
    print("Customer 3:", customer3)

    total, gst = bill_amount(200, gst_rate=0.05)
    print("\nBill total:", total, "GST:", gst)

    show_local()
    show_global()
    counter = make_counter()
    print("Nonlocal counter:", counter(), counter(), counter())
