age= float(input("Enter your age:"))
if age<0:
    print("Invalid entry")
elif age>=0 and age<=12 :
 print("You are a Child ")
elif age>=13 and age<=19:
    print("You are a Teenager")
elif age>=20 and age<=64:
    print("You are an Adult")
else:
    print("You are a Senior")
