year=int(input("enter the year:"))
if year%4==0 or year%400==0:
    print("it is a leap year:")
elif year%100 != 0:
    print("it is not a leap year:")