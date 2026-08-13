status = input("Enter order status:")

if status.lower() == "shipped":
    print("your order has been shipped and is on the way.")
elif status.lower() == "delivered":
    print("Your order has been delivered successfully.")

elif status.lower() =="pending":
    print("your order is pending and will be processed soon.") 

else:
    print("Invalid status. please enter shipped,delivered,or pending.")