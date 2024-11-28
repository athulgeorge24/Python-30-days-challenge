#Task3
set1={34,65,97,22,13}
print(f"The set: {set1}")
print(f"Is the number 3 in the set? {3 in set1}")
print(f"Is the number 65 in the set?{65 in set1}")

#Task4
#attempt to remove elements using discard()
'''
Output:-

The set: {65, 34, 97, 22, 13}
Is the number 3 in the set? False
Is the number 65 in the set?True

The set: {1, 2, 3, 4, 5, 6}
Enter a non-existing number to discard: 22
The set: {1, 2, 3, 4, 5, 6}
Enter a non-existing number to remove: 22
Traceback (most recent call last):
  File "C:\Users\Sandhra Shaji\PycharmProjects\project_1\Amal Shaji MIchael (Day 14).py", line 16, in <module>
    rem=set2.remove(num2)
KeyError: 22

'''
set2={6,5,4,3,2,1}
print(f"\nThe set: {set2}")
num1=int(input(f"Enter a non-existing number to discard: "))
discard=set2.discard(num1)
print(f"The set: {set2}")
#attempt to remove elements using remove()
num2=int(input(f"Enter a non-existing number to remove: "))
rem=set2.remove(num2)
print(f"The set: {set2}")