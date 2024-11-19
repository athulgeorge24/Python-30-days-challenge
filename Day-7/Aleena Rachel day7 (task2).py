order_value= float(input("Enter the total value of your order($):"))
print("Your total order value is:" , order_value, "$") 
if order_value>=50:
  shipping_cost =0.00
  print ("Your shipping cost is($):", shipping_cost) 
elif order_value<50 and order_value>=20:
  shipping_cost= 5.00
  print("Your shipping cost is($):", shipping_cost) 
else:
  shipping_cost= 10.00
  print("Your shipping cost is($):", shipping_cost) 

print("Total cost($):", order_value+shipping_cost) 
