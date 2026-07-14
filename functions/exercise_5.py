def calculate_area(length, width):
    return length * width
def calculate_perimeter(length, width):
    return 2 * (length + width)
def describe_rectangle(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"A {length}x{width} rectangle has an area of {area} and a perimeter of {perimeter}")
length = int(input("Enter the length "))
width = int(input("Enter the width "))
describe_rectangle(length, width)     