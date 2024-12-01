def calculate_area(l,b):
    area=l*b
    return area

n=int(input("No. of arguments: "))

if n==1:
    l1 = int(input(f"Enter side: "))
    b1=l1
    print(calculate_area(l1,b1))
else:
    l1 = int(input(f"Enter length: "))
    b1 = int(input(f"Enter breadth: "))
    print(calculate_area(l1, b1))