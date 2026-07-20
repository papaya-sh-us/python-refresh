def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None


def safe_int_divide(a_text, b_text):
    try:
        a = int(a_text)
        b = int(b_text)
    except ValueError:
        print("Error: please enter valid whole numbers")
        return None

    return safe_divide(a, b)


print(safe_int_divide("10", "2"))
print(safe_int_divide("5", "0"))
print(safe_int_divide("abc", "3"))