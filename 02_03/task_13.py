n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

print("Even?", n % 2 == 0)
print("Binary:", bin(n))
print("Hex:", hex(n))
print("Square:", n ** 2)
