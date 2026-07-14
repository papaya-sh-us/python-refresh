def find_max(numbers):
    if not numbers: #checking for empty list
        return 0
    else:
        max_num = numbers[0]
        for i in numbers:
            if i > max_num:
                max_num = i
        return max_num
def find_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

def input_numbers():
    nums = []
    while True:
        i = input("Enter a number. Type 'end' when you're done ")
        if i == "end":
            break
        try:        #checking for decimal or string input
            nums.append(int(i))
        except ValueError:
            print("Please enter a whole number")
    print("Largest number is ", find_max(nums), " and the sum of the numbers is ",find_sum(nums))

input_numbers()