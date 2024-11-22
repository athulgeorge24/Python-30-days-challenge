Day 10(22/11/24)

# Lists

## Discription:
A `list` in python is a data structure that lets you store multiple items in a single variable. It's flexible and can hold various types of elements, including other lists.
**Key points**
Lists are ordered collections of items.
Lists can contain elements of different data types (e.g., strings, integers, floats).
Lists are indexed, starting at 0 (zero-based indexing).

```python
#syntax:
my_list = [item1, item2, item3, ...]
```
### 1)Creating a list
```
# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "apple", 3.14, True]

# Nested list (list within a list)
nested_list = [[1, 2, 3], ["a", "b", "c"]]
```

### 2)Accessing a list
```
fruits = ["apple", "banana", "cherry"]

# Access the first item
print(fruits[0])  # Output: apple

# Access the last item
print(fruits[-1])  # Output: cherry
```


### 3)Modifying a List
```
fruits = ["apple", "banana", "cherry"]

# Change the second item
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
```

### 4)Adding Elements
```
fruits = ["apple", "banana"]

# Append a new item
fruits.append("cherry")

# Insert an item at a specific index
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry']
```

### 5)Removing Elements
```
fruits = ["apple", "banana", "cherry"]

# Remove by value
fruits.remove("banana")

# Remove by index
popped_item = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
```

### 6)List Slicing
```
# Slicing a list to get a subset of items
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Getting a slice of the list from index 1 to 3 (not including index 3)
slice_of_fruits = fruits[1:3]

# Printing the sliced list
print(slice_of_fruits)

## Expected Output:
python
['banana', 'cherry']

```

## Task:Favorite food

Create a program to manage a list of favorite food  

The program should:

✈Create a list of three favorite food   
✈Ask the user to add a new food to the list  
✈Display the updated list of food  
✈Ask the user to remove one food from the list  
✈Display the final list of food  

Expected output"
```
Current list of food: ['Mandi', 'Al-Faham', 'Noodles']
Enter a food to add: Barbeque
Updated list of food: ['Mandi', 'Al-Faham', 'Noodles','Barbeque']
Enter a food to remove: Al-Faham
Final list of food: ['Mandi','Noodles','Barbeque']

```























































