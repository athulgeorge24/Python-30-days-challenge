#Length of a String
str1=input("Enter a string: ")
str_length=len(str1)
print(f"The length of the sting is {str_length}")

#Conversion of upper case to lower case
str_2=input("Enter a upper  case string: ")
str_lower=str_2.lower()
print(str_lower)

#Conversion of lower case to upper case
str_3=input("Enter a lower case string: ")
str_upper=str_3.upper()
print(str_upper)

#Converts the first character of each word to uppercase
str_4=input("Enter a string: ")
str_title=str_4.title()
print(str_title)

#Swaps uppercase characters to lowercase and vice versa
str_5=input("Enter a string: ")
str_swap=str_5.swapcase()
print(str_swap)

#Capitalizes the first character of the string
str_6=input("Enter a string: ")
str_capital=str_6.capitalize()
print(str_capital)

#String Trimming
str_7=input("Enter a string: ")
str_strip=str_7.strip()
print(str_strip)

#String replacement
str_8="Good luck"
print(f"Old string: {str_8}")
str_8_replace=str_8.replace("luck","bye")
print(f"Replaced string: {str_8_replace}")

#Splits a string into a list of substrings
str_9="Hello Python!"
print(f"Old string: {str_9}")
str_9_split=str_9.split(" ")
print(f"Splitted string: {str_9_split}")

#Joins a list of strings into a single string,
# separated by a specified delimiter
str_10=[f"Hello","Friend"",","how","are","you?"]
print(f"List of string: {str_10}")
str_10_joined=" ".join(str_10)
print(f"Joined string: {str_10_joined}")
