import math
a=float(input("enter a number:"))
b=float(input("Enter another number:"))
#square root of a number

square_root=math.sqrt(a)
square_roota=math.sqrt(b)
print("the square root of number a is:",square_root)
print("the square root of number b is:",square_roota)

#floor of number


floora=math.floor(a)
floorb=math.floor(b)
print("floor of the number a is:",floora)
print("floor of the number b is:",floorb)

#power of number's


power=math.pow(a,b)
powerb=math.pow(b,a)
print("a raised to the power of b:",power)
print("b raised to the power of a:",powerb)


#factorial of numbers

inta=int(a)
intb=int(b)
factoriala=math.factorial(inta)
factorialb=math.factorial(intb)
print("factorial of number a is:",factoriala)
print("factorial of number b is:",factorialb)


#log of number's


y=math.log(a)
x=math.log(b)
print("logarithm of the number a is :",y)
print("logarithm of the number b is :",x)


#math.pi,#math.e

print("value of pi is",math.pi)
print("value of e is",math.e)