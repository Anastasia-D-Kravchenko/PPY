s = input("Type something: ")

print("concatenation with text:", s + "abc", end="\n\n")
try:
    print("addition with number:", s + 5, end="\n\n")
except TypeError as e:
    print("error:", e, end="\n\n")

print("multiplication by number:", s * 3, end="\n\n")
try:
    print("multiplication by text:", s * "a", end="\n\n")
except TypeError as e:
    print("error:", e, end="\n\n")

try:
    print("division by number:", s / 2, end="\n\n")
except TypeError as e:
    print("error:", e, end="\n\n")
