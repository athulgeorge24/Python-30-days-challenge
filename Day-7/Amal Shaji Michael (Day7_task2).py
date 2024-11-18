#Online order shipping cost
total_value=float(input("Enter the total value of your order($): "))
shipping_cost_1=5.00
shipping_cost_2=10.00
if total_value>=50:
    print(f"Your total order value: ${total_value}")
    print("Your shipping cost: $0")
    print(f"Total cost (order value + shipping): ${total_value}")
elif total_value>=20 and total_value<50:
    print(f"Your total order value: ${total_value}")
    print(f"Your shipping cost: ${shipping_cost_1}")
    print(f"Total cost (order value + shipping): ${total_value+shipping_cost_1}")
elif total_value>0 and total_value<20:
    print(f"Your total order value: ${total_value}")
    print(f"Your shipping cost: ${shipping_cost_2}")
    print(f"Total cost (order value + shipping): ${total_value + shipping_cost_2}")
else:
    print("Invalid input!")