# --- PPY SURPRISE EXAM PREP (PART 3): ADVANCED PYTHONIC CONCEPTS ---
# Based on PPY03eng.pdf: Comprehensions, Lambda, *args/**kwargs, and Predicates.

# 1. THE "INVERTED DICTIONARY" (SETS + COMPREHENSIONS)
# Trick: Using one comprehension to count and another nested one to group by frequency.
def group_by_frequency(text):
    # Step 1: Dictionary comprehension to count occurrences of each unique character [cite: 1085]
    counts = {char: text.count(char) for char in set(text)}

    # Step 2: Nested dictionary/set comprehension to invert the logic [cite: 1080, 1085]
    # We iterate over unique frequencies to create keys, then filter original items as the set value
    inverted = {freq: {k for k, v in counts.items() if v == freq} for freq in set(counts.values())}
    return inverted


print(f"1. Frequency Map: {group_by_frequency('abracadabra')}")

# 2. THE "PREDICATE FILTER COMBO" (HIGHER-ORDER FUNCTIONS)
# Trick: Using *args to pass multiple functions and all() to verify them.
is_even = lambda x: x % 2 == 0  # Lambda function syntax [cite: 1207]
is_positive = lambda x: x > 0
is_less_than_100 = lambda x: x < 100


def filter_all(data, *predicates):
    """Returns elements that return True for ALL predicate functions passed in *args."""[cite: 1216]
    # filter() applies the lambda to every element; all() checks all conditions [cite: 1157, 1163]
    result = filter(lambda x: all(p(x) for p in predicates), data)
    return list(result)


test_data = [-10, 2, 50, 99, 102, -5]
print(f"2. Predicate Filter: {filter_all(test_data, is_even, is_positive, is_less_than_100)}")

# 3. ADVANCED SORTING WITH LAMBDA
# Trick: Sorting by multiple criteria (one descending, one ascending) using a tuple key.
students = [("Alice", 20, 85), ("Bob", 22, 90), ("Charlie", 21, 90), ("Dave", 19, 85)]

# sorted() returns a new list[cite: 1124].
# Key logic: -x[2] (score) makes it descending; x[0] (name) remains ascending. [cite: 1140, 1150]
sorted_students = sorted(students, key=lambda x: (-x[2], x[0]))
print(f"3. Multi-Criteria Sort: {sorted_students}")

# 4. ZIP() + ENUMERATE() IN ONE LINE
# Trick: Combining parallel iteration and indexing in a single comprehension.
keys = ['name', 'age', 'city', 'job', 'country']
values = ['Anna', 25, 'Warsaw', 'Dev', 'Poland']

# zip() pairs lists [cite: 1161]; enumerate() adds index[cite: 1160].
# Condition 'i % 2 == 0' filters for even-indexed items only. [cite: 1073]
filtered_dict = {k: v for i, (k, v) in enumerate(zip(keys, values)) if i % 2 == 0}
print(f"4. Filtered Zip Dict: {filtered_dict}")


# 5. **KWARGS AS CONFIGURATION SETTINGS
# Trick: Use .get() on **kwargs to provide default behavior if a key is missing.
def process_data(*args, **kwargs):
    # Check for 'filter_negatives' flag in keyword arguments [cite: 1222]
    data = [x for x in args if x >= 0] if kwargs.get('filter_negatives', False) else args

    action = kwargs.get('action', 'sum')  # Default action is 'sum' [cite: 1199]
    if action == 'sum':
        return sum(data)
    elif action == 'max':
        return max(data)


print(f"5a. Sum (Filtered): {process_data(10, -5, 20, action='sum', filter_negatives=True)}")
print(f"5b. Max (Unfiltered): {process_data(10, -5, 20, action='max')}")

# --- FINAL EXAM CRITICAL NOTES ---
# - Generators: (expr for x in y) creates an object, not data. Use list() to view. [cite: 1094]
# - Unpacking: 'a, b = (1, 2)' is why 'for k, v in dict.items()' works. [cite: 1040, 1063]
# - Tuple Immutability: You cannot .append() to a tuple. [cite: 1035]
#   To add: new_tuple = old_tuple + (item,)  <-- Must include the trailing comma!