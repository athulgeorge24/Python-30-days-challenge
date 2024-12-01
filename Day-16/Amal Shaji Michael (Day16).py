#Task3
list1 = []
def process_numbers():
    print("Enter the elements: ")
    for i in range(n):
        element = int(input("\t"))
        if element>10 and element%5!=0:
            list1.append(2*element)
    return list1
n = int(input("Enter the no.of elements: "))
print(process_numbers())

#Task4
def sum_of_digits(number):
    if number<10:
        return number
    else:
        return sum_of_digits(number%10)+sum_of_digits(number//10)
num=int(input("Enter the number: "))
print(f"Sum of digits: {sum_of_digits(num)}")