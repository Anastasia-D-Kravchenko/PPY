# --- PPY SURPRISE EXAM PREP: CONSOLIDATED CODE SNIPPET ---

# 1. THE "TYPE-CHECKING" *ARGS TRAP
# Combining: *args, type checking, and string methods [cite: 5, 155, 219, 801, 1216]
def smart_sum(*args):
    """
    Accepts mixed types, ignores text, converts numeric strings, sums numbers.
    """
    total = 0
    for item in args:
        # Check if already a numeric type [cite: 155]
        if type(item) in (int, float):
            total += item
        # Check if string is numeric before casting [cite: 219]
        elif type(item) == str and item.isdigit():
            total += int(item)
    return total

print(f"Smart Sum: {smart_sum(10, 'hello', 5.5, '20')}") # Expected: 35.5


# 2. THE "DICTIONARY FLIPPER" WITH A TWIST
# Combining: String splitting, lowercasing, and grouping into sets [cite: 113, 223, 736, 1041]
text = "Python is great and python is fun"
words = text.lower().split() # Standardize and tokenize [cite: 208, 224]

length_dict = {}
for word in words:
    length = len(word) # Get criteria for key [cite: 201]
    if length not in length_dict:
        length_dict[length] = set() # Initialize set to handle unique words [cite: 1041]
    length_dict[length].add(word) # Sets automatically prevent duplicates [cite: 1044, 1047]

print(f"Length Dictionary: {length_dict}")


# 3. ONE-LINER COMPREHENSIONS WITH ZIP()
# Combining: Dictionary comprehensions and parallel iteration [cite: 1085, 1161]
names = ["Alice", "Bob", "Charlie", "Dave"]
scores = [85, 42, 90, 30]

# Mapping names to scores only if they passed (score > 50) [cite: 1088, 1091, 1178]
passed_students = {name: score for name, score in zip(names, scores) if score > 50}

print(f"Passed Students: {passed_students}")


# 4. ADVANCED WHILE LOOP WITH SETS
# Combining: Infinite loops, user input, and set subset logic [cite: 146, 507, 751, 1045]
def check_vowels():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    print("\n--- Enter words until one contains all vowels ---")
    while True: # Loop until break [cite: 512, 962]
        word = input("Enter a word: ").lower()
        # Convert word to set for comparison [cite: 1045, 1174]
        if vowels.issubset(set(word)):
            print(f"Success! '{word}' contains all vowels.")
            break # Exit loop immediately [cite: 515, 963]
        print("Keep trying...")


# 5. **KWARGS AND FORMATTING
# Combining: Keyword argument packing and string formatting [cite: 806, 885, 1222]
def build_profile(first, last, **kwargs):
    """
    Returns formatted profile with capitalized keys and titled names.
    """
    # Use f-strings for formatting [cite: 63]
    profile = f"Name: {first.title()} {last.title()}\n"

    # kwargs acts as a dictionary [cite: 1063, 1228]
    for key, value in kwargs.items():
        profile += f"{key.upper()}: {value}\n" # upper() from Class 1 [cite: 226]

    return profile

print(f"Profile:\n{build_profile('john', 'doe', age=30, city='Warsaw')}")


# 6. FILTER AND LAMBDA MADNESS
# Combining: Functional programming and string validation [cite: 1163, 1183, 1207]
words_list = ["Hello", "Pyth0n", "Hi", "World!", "Coding"]

# Lambda checks for alpha-only characters and specific length [cite: 221, 1210]
valid_words = list(filter(lambda w: w.isalpha() and len(w) > 4, words_list))

print(f"Filtered Words: {valid_words}")


# --- EXAM REMINDERS ---
# 1. input() always returns 'str'. Cast to 'int()' for math[cite: 147, 167].
# 2. Tuples are immutable[cite: 1035]. To change: list(t) -> modify -> tuple(l)[cite: 864, 868].
# 3. Always use .items() to iterate through dict keys and values simultaneously[cite: 1063, 1173].