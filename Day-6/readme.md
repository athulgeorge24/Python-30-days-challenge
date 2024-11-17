Day 6 (17/11/24)

# Learn to use Conditional statements and logical operators

## 1)Logical Operators

### Description:  
Logical operators are used to combine conditional statements or check multiple conditions at once. Python supports 3 logical operators:  

`and`: Returns `True` if both conditions are true.  
`or`: Returns `True` if at least one condition is true.  
`not`: Reverses the result of a condition.  

## 2)Conditional Statements

## a) if statement

### Description:
The `if` statement is used for making decision in Python.It executes a block of code if the condition evaluates to `True`.
```python
#Syntax:

if condition:
    # code to execute if the condition is true
```

## b) if-else Statement

### Description:
The `if-else` statement provides an alternative block of code to execute if the condition is `False`.
```python
#Syntax:

if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```

## c) if-elif-else Statement:
The `if-elif-else` statement is used to check multiple conditions. It executes the first block where the condition evaluates to `True`. If none of the conditions are `True`, the else block executes.
```python
#Syntax:

if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if no conditions are true

```



## Task 1: Login to a system with Username and Password
Create a simple login system where the user is need to enter their username and password. The program should check if both are correct:  
(You can give username and password as your wish)  

 ◐Username: "alpha"(username)    
 ◐Password: "unknown@000"(password)  
 
If both are correct, print "Login successful", otherwise print "Login failed".    

## Expected output
```python
Enter your username : alpha
Enter your password : unknown@000
Login successfull
```

## Task 2 : Age Group Classifier
Write a program that takes an age as input and classifies the person into an age group of:

◐`"Child"` if the age is between 0 and 12.  
◐`"Teenager"` if the age is between 13 and 19.  
◐`"Adult"` if the age is between 20 and 64.  
◐`"Senior"` if the age is 65 or older.  

## Expecter output
```python
Enter your age : 23
You are an adult
```

## Task 3 : Speeding Ticket
Write a program that takes the speed of a vehicle as input and checks if the driver is speeding or not:  

◐ The speed limit is 70 km/h.  
◐ If the vehicle is traveling faster than 70 km/h, print "You are speeding. You will receive a ticket."  
◐ If the vehicle is traveling at or below 70 km/h, print "You are within the speed limit."  

## Expected output
```python
Enter the speed(km/h) : 80
You are speeding. You will receive a ticket
```




