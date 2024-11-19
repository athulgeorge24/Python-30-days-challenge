from unittest import removeResult

string="pyTHoN"
length = len(string)
lower = string.lower()
upper = string.upper()
title = string.title()
swap = string.swapcase()
capital = string.capitalize()
strip = string.strip()


print(length)
print(lower)
print(upper)
print(title)
print(swap)
print(capital)
print(strip)

s = "green apple"
result = s.replace("green", "orange")
print(result)

sa = "Hello, World!"
print(sa.split(","))

sb = ['Hello', 'World']
print(" ".join(sb))
