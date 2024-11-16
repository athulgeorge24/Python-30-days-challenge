#length of string
str_1=input("enter a string:")
str_length=len(str_1)
print(str_length)
#string case conversion
#to lower 
a=input("enter a string in upper case:")
lower=a.lower()
print(lower)
#to upper
b=input("enter a word in lower case:")
upper=b.upper()
print(upper)
#title()
c=input("enter a string:")
title=c.title()
print(title)
#swaping upper to lower and viceversa
d=input("write something in upper or lower case:")
swap=d.swapcase()
print(swap)
#capitalise
e=input("enter a string with first character as small letter:")
capital=e.capitalize()
print(capital)
#strip
f=input("enter a string:")
strip=f.strip()
print(strip)
a="you are"
b=a.replce("you",we)
print(b)
y="hi athul"
print(y.split(","))
z=['hi', 'athul']
print("".join(z))