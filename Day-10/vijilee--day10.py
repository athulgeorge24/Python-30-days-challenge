fruits=["Biriyani","mandhi","porotta"]
print(fruits)
new_food=input("enter a new food which you like...:")
fruits.append(new_food)
print(fruits)
removing_food=input("enter an item which is to be removed from the list:")
fruits.remove(removing_food)
print(f"final list of the food is{fruits}")