
age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif 20 <= age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")