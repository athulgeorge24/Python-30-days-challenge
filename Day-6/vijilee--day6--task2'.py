age=int(input("enter the age :"))
if age<=12:
    print("you are a child...")
elif age>13 and age<19:
    print("you are Teenager")
elif age>19 and age<64:
    print("you are an adult:")
elif age>64:
    print("you are a senior citizen:")
else:
    print("age can't be negative:")