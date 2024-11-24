Day 12(24/11/24)

# Tuples

A `tuple` is an ordered collection of elements, similar to a list, but immutable (cannot be modified after creation).
`Tuples` are defined by enclosing elements in *parentheses ()*.  

```
Example:
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # Output: (1, 2, 3, 4)
`````
## 1)Creating and Accessing Tuples
Tuples can contain any type of object, and they are accessed using indices, just like lists.

**Creating a Tuple:**
```
# A tuple with integers
numbers = (1, 2, 3)

# A tuple with mixed data types
person = ("Alice", 30, "Engineer")

# A tuple with a single element (comma is important)
single_element_tuple = (5,)
```
**Accessing Elements:**
You can access individual elements of a tuple by indexing (starting at 0) or by slicing.
```
# Accessing individual elements
print(person[0])  # Output: Alice
print(person[1])  # Output: 30

# Slicing a tuple
print(person[1:])  # Output: (30, 'Engineer')
```
## 2)Tuple Operations

Tuples support several operations such as slicing, concatenation, and repetition.

**a)Slicing**: You can slice a tuple to get a subset of elements.
```
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # Output: (2, 3, 4)
```
**b)Concatenation**: You can concatenate two tuples using the + operator.
```
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)
```
**c)Repetition**: You can repeat a tuple multiple times using the * operator.
```
numbers = (1, 2)
repeated = numbers * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)
```
**d)Immutability of Tuples**: Unlike lists, tuples are immutable, meaning their elements cannot be changed after the tuple is created.
```
Example of Immutability:
my_tuple = (1, 2, 3)
# This will raise an error because tuples cannot be changed
my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment
```
However, you can create a new tuple if you want to change its contents.
```
# Create a new tuple by concatenating existing tuples
new_tuple = my_tuple[:2] + (10,) + my_tuple[2:]
print(new_tuple)  # Output: (1, 2, 10, 3)
```
## 3)Tuple Methods

Tuples have a few built-in methods that can be useful for certain operations. 

*-> `count()`*:Counts how many times an element appears in the tuple.
```
my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3
```
*-> `index()`* ::Returns the index of the first occurrence of an element.
```
my_tuple = (1, 2, 3, 4)
print(my_tuple.index(3))  # Output: 2
```


# Tasks
## Task 1:

**Create a Tuple**
Create a tuple that contains the names of three countries you'd like to visit.
Print the first and the last country from the tuple.

## Task 2:

Create two tuples:
**Tuple Concatenation**
One with the names of three favorite animals.
One with the names of three favorite birds.
Concatenate them into a new tuple and print it.

## Task 3

**Immutability**
Attempt to remove an element from a tuple and catch the error.
Then, create a new tuple by removing one specific value (hint: use slicing).

## Task 4

**Tuple Methods**
Create a tuple with some repeated elements (e.g., numbers or strings).
Use the count() method to find how many times a specific value appears.
Use the index() method to find the position of a specific value.

## Task 5

**Nested Tuple**
Create a tuple that contains three other tuples (e.g., one for fruits, one for vegetables, and one for drinks).
Print the second element of the second tuple.



















