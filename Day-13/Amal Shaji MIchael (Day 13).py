#Task1
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
union=set1|set2
print(f"Union: {union}")
intersection=set1&set2
print(f"Intersection: {intersection}")
difference=set2-set1
print(f"Difference: {difference}")
symmetric_diff=set1^set2
print(f"Symmetric difference: {symmetric_diff}")

#Task2
set3={22,83,45,16,78}
print(f"\nThe set: {set3}")
num_1=int(input("Enter a number to add: "))
set3.add(num_1)
num_2=int(input("Enter another number to add: "))
set3.add(num_2)
print(f"The set: {set3}")
num_3=int(input("Enter an existing number to remove: "))
set3.remove(num_3)
print(f"The set: {set3}")
num_4=int(input("Enter a non-existing number to discard: "))
set3.discard(num_4)
print(f"The set: {set3}")
clear=input("Enter 'clear' to empty the set: ")
if clear=="clear":
    set3.clear()
    print(f"Contents of the set: {set3}")
else:
    print("Invalid Entry!")