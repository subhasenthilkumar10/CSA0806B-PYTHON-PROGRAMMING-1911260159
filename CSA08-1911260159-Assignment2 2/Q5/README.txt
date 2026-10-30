Q5 notes
A mutable default list is created once when the function is defined. Each
call to add_item_buggy uses the same list, so Tea and Vada appear together.
The corrected function uses None as the default and creates a new list
inside the function for each call.

Positional arguments are matched by order. Keyword arguments are matched
by parameter name. Default parameters are used when an argument is omitted.
A function can return multiple values as a tuple, such as (total, GST).

Local names exist inside a function. Global names are defined at module
level. nonlocal refers to a name in an enclosing function. To reassign a
global name inside a function, global is needed; it is usually avoided
because shared state makes code harder to test and maintain.

The default-list bug can be inspected with add_item_buggy.__defaults__.
Each append is O(1) on average; each customer's list uses O(m) space for
m items. Passing a list explicitly also takes O(1) per append. A closure
can keep a private list, but it still stores O(m) items.
