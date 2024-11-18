#Leap year calculator
year=int(input("Enter a year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("The given year is a Leap year.")
else:
    print("The given year is not a Leap year.")
