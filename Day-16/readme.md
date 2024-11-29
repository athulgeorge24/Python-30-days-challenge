Day 16(29/11/24)
# Functions in Python(Continuation)

## Task 3: Functions with Loops and Conditionals

*Create a function to process a list of numbers and filter them based on specific criteria using loops and conditionals.

Write a function called `process_numbers` that takes a list of integers as input 
### Inside the function:
### a)Filter Criteria:
->Keep only numbers greater than 10  
->Remove numbers divisible by 5  
### b)Transformation:
->Double the remaining numbers  
#### c)Return the final list after filtering and transformation  

Expected Input:
```python

numbers = [4, 15, 8, 12, 25, 11, 7, 30, 13]
```
Expected Output:

```python
[24, 22, 26]

#Explanation
#Numbers > 10: [15, 12, 25, 11, 30, 13]
#After removing numbers divisible by 5: [12, 11, 13]
#After doubling: [24, 22, 26]
```

## Task 4:Recursive Function

*Use recursion to calculate the sum of the digits of a given positive integer  

Write a recursive function called sum_of_digits that takes a positive integer n as input  
### The function should return the sum of all its digits, where:  
->Base Case: If `n < 10`, return `n` (a single digit is its own sum)  
->Recursive Case: Return the last digit of `n` `(n % 10)` plus the sum of the remaining digits `(n // 10)`  
Test the function with several numbers like `123`,` 9876`, and `5`


Example Input:
```python

sum_of_digits(123)
```
Expected Output:
```python
6  # (1 + 2 + 3)
```

**Steps to Solve:**

Define the function sum_of_digits(n):
-> Check if n < 10. If true, return n  
-> Otherwise, add the last digit of n (n % 10) to the result of sum_of_digits(n // 10) (the number without the last digit)  
->Test the function with different inputs  


















