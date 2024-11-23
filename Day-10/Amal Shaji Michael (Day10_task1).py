#Favorite food
'''
Output:-
Current list of food: ['Mandhi', 'Al-Faham', 'Noodles']
Enter a food to add: Barbeque
Updated list of food: ['Mandhi', 'Al-Faham', 'Noodles', 'Barbeque']
Enter a food to remove: Al-Faham
Final list of food: ['Mandhi', 'Noodles', 'Barbeque']
'''
food=['Mandhi','Al-Faham','Noodles']
print(f"Current list of food: {food}")
add_food=input("Enter a food to add: ")
food.append(add_food)
print(f"Updated list of food: {food}")
remove_food=input("Enter a food to remove: ")
food.remove(remove_food)
print(f"Final list of food: {food}")