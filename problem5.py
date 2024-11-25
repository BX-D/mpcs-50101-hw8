#Function to check whether number can be used in special algorithm
def is_divisible_by_11(number):
    if isinstance(number, int):
        nums = str(number)
        sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
               sum += int(nums[i])
            else:
               sum -= int(nums[i])
        if sum % 11 == 0:
            print("This is divisible by 11.")
            return True
    print("This is not divisible by 11.")
    return False

num = int(input("Enter a number: "))
is_divisible_by_11(num)