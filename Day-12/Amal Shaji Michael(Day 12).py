#Task1
countries=("America","Canada","Brazil")
print(countries[0])
print(countries[2])

#Task2
fav_animals=("Dog","Cat","Rabbit")
fav_birds=("Peacock","Pigeon","Parrot")
favorites=fav_animals+fav_birds
print(favorites)

#Task3
tuple_1=(1,2,3)
#tuple_1[0]=10 #Error
tuple_2=tuple_1[0:2]
print(tuple_2)

#Task4
tuple_3=(1,"cat",2,"apple",1,5,2,"cat",1)
rep_tuple3=tuple_3*2
print(rep_tuple3.count(1))
print(rep_tuple3.index("cat"))

#Task5
fruits=("apple","orange","grapes","dates")
vegetables=("cucumber","carrot","lady's finger","tomato")
drinks=("tea","coffee","fresh lime","milkshake")
food=(fruits,vegetables,drinks)
print(vegetables[1:2])