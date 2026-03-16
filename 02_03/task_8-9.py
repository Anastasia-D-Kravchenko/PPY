import sys

n = 255
print(bin(n))
print(oct(n))
print(hex(n))

print(int("1111", 2))
print(int("FF", 16))
print(int("17", 8))

# x = 2 ** 200000
# print(x)
# print(type(x))

# Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

sys.set_int_max_str_digits(4301)

x = 2 ** 200000
print(x)
print(type(x))