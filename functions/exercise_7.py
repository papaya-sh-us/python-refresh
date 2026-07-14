def sum_of_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum
nums = [1,4,6,8,2,10]
print(sum_of_list(nums))