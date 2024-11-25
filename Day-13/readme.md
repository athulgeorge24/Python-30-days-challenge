Day 13(25/11/24)

# Sets in Python

☛A set is an unordered collection of unique elements  
☛Sets are mutable, but their elements must be immutable (e.g., numbers, strings, or tuples)  
☛Sets are commonly used to store distinct items and perform mathematical set operations like union, intersection, and difference  

## 1) Creating and Accessing Sets

### a)Creating a Set:

Sets are created using curly braces {} or the built-in set() function.
```python

# A set with integers
numbers = {1, 2, 3, 4}

# A set with mixed data types
mixed_set = {"Alice", 30, 5.5}

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set
```
### b)Accessing Elements:
Since sets are unordered, they do not support indexing or slicing. To access elements, you can use iteration.

```python

# Iterating over a set
for num in numbers:
    print(num)
```
## 2) Set Operations
Sets support various operations for managing and comparing their elements.

### a) Adding and Removing Elements:
```python

my_set = {1, 2, 3}

# Adding an element
my_set.add(4)  # {1, 2, 3, 4}

# Removing an element
my_set.remove(2)  # {1, 3, 4} (raises KeyError if the element does not exist)

# Discarding an element (does not raise an error if the element is missing)
my_set.discard(5)

# Removing all elements
my_set.clear()  # set()
```
### b) Mathematical Set Operations:
Sets support operations like union, intersection, difference, and symmetric difference.

```python

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (all unique elements from both sets)
print(set1 | set2)  # {1, 2, 3, 4, 5}

# Intersection (common elements)
print(set1 & set2)  # {3}

# Difference (elements in set1 but not in set2)
print(set1 - set2)  # {1, 2}

# Symmetric Difference (elements in either set, but not both)
print(set1 ^ set2)  # {1, 2, 4, 5}

```

# Tasks:


## Task 1: Set Operations - Mathematical Operations
Create two sets:
```
#Eg:
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
```
Perform the following operations and print the results:

☛Union of `set1` and `set2`  
☛Intersection of `set1` and `set2`  
☛Difference of `set1` from `set2`  
☛Symmetric Difference of `set1` and `set2`  

## Task 2: Adding and Removing Elements

Create a set containing five random numbers  

☛Add two new numbers to the set using the `add()` method  
☛Remove one existing number using the `remove()` method  
☛Try discarding a number that doesn’t exist using the `discard()` method  
☛Clear the set and print its contents to confirm it is empty  














