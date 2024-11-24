food_list=['Mandhi','Al-Faham','Noodles']
while True:
    print("Select your choice: ")
    print("1.\tShow food list: ")
    print("2.\tAdd Food: ")
    print("3.\tRemove Food: ")
    print("4.\tExit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(food_list)
    elif choice==2:
        add=input("Enter a food to add: ")
        food_list.append(add)
        print("Updated List: ")
        print(f"\n{food_list}")
    elif choice==3:
        rem=input("Enter a food to remove: ")
        food_list.remove(rem)
        print("Updated List: ")
        print(f"\n{food_list}")
    elif choice==4:
        print("Thank You!")
        break
    else:
        print("Invalid Entry!")
