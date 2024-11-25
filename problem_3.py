def greatest_common_divisor(a,b):   
 # return the greatest common divisor
 divisor = min(a, b)
 while divisor > 0:
    if a % divisor == 0 and b % divisor == 0:
        print(f"The greatest common divisor of a and b is {divisor}")
        return True
    divisor -= 1

try:
    a = int(input("please enter a number of a: "))
    b = int(input("please enter a number of b: "))
    greatest_common_divisor(a, b)
except:
    print("Please enter number.")
    