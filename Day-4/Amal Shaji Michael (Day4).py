#Square root of a number
import math
num_1=int(input("Enter a number: "))
sq_root=math.sqrt(num_1)
print(f"The square root of {num_1} is {sq_root}")

#Greatest integer of a number
num_2=float(input("Enter a number: "))
floor_fn=math.floor(num_2)
print(f"The greatest integer of {num_2} is {floor_fn}")

#Power of a number
num_3=float(input("Enter a number: "))
num_4=float(input("Enter a number to be raised: "))
power=math.pow(num_3,num_4)
print(f"{num_3} to the power of {num_4} is {power}")

#Factorial of a number
num_5=int(input("Enter a number: "))
fact=math.factorial(num_5)
print(f"The factorial of {num_5} is {fact}")

#Natural logarithm of a number
num_6=float(input("Enter a number: "))
nat_log=math.log(num_6)
print(f"The natural logarithm of {num_6} is {nat_log}")

#Constants in math module
print(f"Value of pi is {math.pi}")
print(f"Value of Euler's number is {math.e}")

# Inverse Trignometric Functions
x=float(input("Enter a number to find its\ninverse trignometric values: "))
sine=math.asin(x)
print(f"sin({x}): {sine}")
cosine=math.acos(x)
print(f"cos({x}): {cosine}")
tangent=math.atan(x)
print(f"tan({x}): {tangent}")
