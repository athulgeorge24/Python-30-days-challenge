def multiply_numbers(a,b):
    product=(a*b)
    return product
a1=int(input("Enter a number: "))
b1=int(input("Enter another number: "))
print(f"Product: {multiply_numbers(a1,b1)}")

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
n1=int(input("Enter a number to check whether even or not: "))
print(is_even(n1))