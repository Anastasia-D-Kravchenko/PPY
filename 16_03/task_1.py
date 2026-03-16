def task_1():
    cart = {}

    print("Add products to your cart. Type 'done' as the product name to finish.")
    while True:
        product = input("Enter product name: ")
        if product.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {product}: "))
            cart[product] = price
        except ValueError:
            print("Invalid price. Please enter a number.")

    if cart:
        total_value = sum(cart.values())
        most_expensive = max(cart, key=cart.get)
        average_price = total_value / len(cart)

        print("\n--- Cart Summary ---")
        for item, price in cart.items():
            print(f"- {item}: ${price:.2f}")
        print(f"Total Value: ${total_value:.2f}")
        print(f"Most Expensive Product: {most_expensive} (${cart[most_expensive]:.2f})")
        print(f"Average Price: ${average_price:.2f}")
    else:
        print("Your cart is empty.")

task_1()