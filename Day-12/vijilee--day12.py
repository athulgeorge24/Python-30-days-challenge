countries=("England","Spain","Brazil")
print(countries[0]),print(countries[2])

#concatination
animals=("Tiger","Elephent","Dolphin")
birds=("peacock","parrot","crow")
combined_tuple=animals+birds
print(combined_tuple)
#removing
a=("albin","amal","me")
b=a[1:]
print(b)
#methods
a=(1,2,3,4)
repeated=a*4
print(repeated)
print(repeated.count(2))
print(a.index(3))
#nested tuple
a=(1,2,3)
b=(4,5,6)
c=(7,8,9)
nested_tuple=(a,b,c)
print(nested_tuple)