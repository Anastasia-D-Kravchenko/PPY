s = input("Enter a sentence: ")
print("Length:", len(s))
print("Spaces -> _:", s.replace(" ", "_"))
words = s.split()
print("List of words:", words)
print("First 3 characters:", s[:3])
print("Last 4 characters:", s[-4:])

print("Number of words:", len(words))

digits_count = sum(ch.isdigit() for ch in s)
print("Number of digits:", digits_count)

t = input("Enter a value to check: ")
print("isdigit:", t.isdigit())
print("isalpha:", t.isalpha())

s2 = input("Enter a sentence to check: ")
print("'Python' in sentence?", "Python" in s2)
print("How many times 'a'?:", s2.count("a"))
print("Replace Python->JAVA:", s2.replace("Python", "JAVA"))
