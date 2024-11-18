#Length of a String
str_1=input("Enter a sentence ")
str_length=len(str_1)
print("The length of the sting is",str_length)

#Conversion of upper case to lower case
str_lower=str_1.lower()
print(str_lower)

#Conversion of lower case to upper case
str_upper=str_1.upper()
print(str_upper)

#Converts the first character of each word to uppercase
str_title=str_1.title()
print(str_title)

#Swaps uppercase characters to lowercase and vice versa
str_swap=str_1.swapcase()
print(str_swap)

#Capitalizes the first character of the string
str_capital=str_1.capitalize()
print(str_capital)

#String Trimming
str_strip=str_1.strip()
print(str_strip)

#String replacement
str_2="Good luck"
print("Old string:",str_2)
str_2_replace=str_2.replace("luck","bye")
print("Replaced string:", str_2_replace)

#Splits a string into a list of substrings
str_3="Hello Python!"
print("Old string:",str_3)
str_3_split=str_3.split(" ")
print("Splitted string:", {str_3_split})

#Joins a list of strings into a single string,
# separated by a specified delimiter
str_4=["Hello","Friend",",","how","are","you?"]
print("List of string:", str_4)
str_4_joined=" ".join(str_4)
print("Joined string:", str_4_joined)
