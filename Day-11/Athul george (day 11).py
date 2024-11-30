from random import choice

food = ["Mandhi", "Al-Faham", "Noodles"]
while True:
    print("Select your choice:")
    print("1. Show food list")
    print("2. Add Food: ")
    print("3. Remove food: ")
    print("4. Exit")
    print()
    choice=int(input("Enter your choice: "))

    if choice == 1:
        for i in food:
            print(food.index(i) + 1,i, end=" ")
            print()
        print()
    elif choice==2:
        add_food = input("Enter a food to add:")
        print("Updated list")
        food.append(add_food)
        for i in food:
            print(food.index(i) + 1, i, end=" ")
            print()
        print()
    elif choice==3:
        remove_food = input("Enter a food to remove:")
        if remove_food in food:
            food.remove(remove_food)
        print("Updated list")

        for i in food:
            print(food.index(i) + 1, i, end=" ")
            print()
        print()
    elif choice==4:
        print ("Thank you!!")
        break

    else:
        print("Invalid input!!")


   