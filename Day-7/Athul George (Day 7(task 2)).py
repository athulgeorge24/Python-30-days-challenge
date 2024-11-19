order_value = float(input("Enter the total value of your order ($): "))

if order_value >= 50:
    shipping_cost = 0
elif order_value >= 20:
    shipping_cost = 5
else:
    shipping_cost = 10

total_cost = order_value + shipping_cost

print(f"Your total order value: ${order_value:.2f}")
print(f"Your shipping cost: ${shipping_cost:.2f}")
print(f"Total cost (order value + shipping): ${total_cost:.2f}")