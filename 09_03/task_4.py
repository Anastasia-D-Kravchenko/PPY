mock_inputs = [19.99, 5.50, 42.00, 15.75, 0]
prices = []

for p in mock_inputs:
    if p == 0:
        break
    prices.append(p)

if prices:
    total = sum(prices)
    most_expensive = max(prices)
    avg_price = total / len(prices)
    reverse_order = prices[::-1]

    print(f"Total price: {total:.2f}")
    print(f"Most expensive product: {most_expensive}")
    print(f"Average price: {avg_price:.2f}")
    print(f"Reverse order: {reverse_order}")
print("-" * 30)