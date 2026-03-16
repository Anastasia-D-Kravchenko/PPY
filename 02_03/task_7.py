n = int(input("Enter a number: "))

if n > 0 and n % 2 == 0:
    print("Number is positive and even")

if n < 0 or n > 100:
    print("Number is negative or greater than 100")

if not (n % 2 == 1):
    print("Number is not odd (so it is even)")