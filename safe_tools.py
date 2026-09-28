def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))

def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


print(safe_number("42"))
print(safe_number("hello"))

def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


learner = {
    "name": "Shukuru",
    "age": 18
}

print(get_field(learner, "name"))
print(get_field(learner, "email"))