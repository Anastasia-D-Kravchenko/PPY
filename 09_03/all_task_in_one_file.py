import random


# ==========================================
# 1. MAIN TASKS
# ==========================================

def main_tasks():
    print("=== 1. MAIN TASKS ===")

    # Task 1: Student Scores
    scores = [random.randint(0, 100) for _ in range(50)]
    grades = [5 if s >= 90 else 4 if s >= 75 else 3 if s >= 60 else 2 for s in scores]
    avg_score = sum(scores) / 50
    passed = sum(1 for g in grades if g > 2)
    best_5 = sorted(scores, reverse=True)[:5]
    # Expected: avg ~50, passed variable based on random, best_5 values near 100
    print(f"Task 1: Avg={avg_score}, Passed={passed}, Top 5={best_5}")

    # Task 2: Guessing Game (Logic Simulation)
    target = random.randint(1, 100)
    attempts = 0
    guesses = []
    # Mocking a quick success for demonstration
    sim_guess = 0
    while sim_guess != target:
        attempts += 1
        sim_guess = random.randint(1, 100)
        guesses.append(sim_guess)
        if attempts > 1000: break  # Safety break
    # Expected: attempts variable, last 3 guesses from the list
    print(f"Task 2: Attempts={attempts}, Last 3 Guesses={guesses[-3:]}")

    # Task 3: Numerical Data
    data = [random.randint(1, 100) for _ in range(20)]
    avg_val = sum(data) / 20
    above_avg = sum(1 for x in data if x > avg_val)
    evens = [x for x in data if x % 2 == 0]
    every_second = data[::2]
    second_largest = sorted(list(set(data)))[-2] if len(set(data)) > 1 else None
    # Expected: avg ~50, list of evens, second highest value in list
    print(f"Task 3: Avg={avg_val}, Above Avg Count={above_avg}, Evens={evens}, 2nd Max={second_largest}")

    # Task 4: Shopping Cart (Simulation)
    cart = [12.5, 45.0, 9.99, 0]  # 0 is the stop signal
    prices = [p for p in cart if p > 0]
    total = sum(prices)
    most_exp = max(prices) if prices else 0
    reverse_cart = prices[::-1]
    # Expected: total=67.49, max=45.0, reverse=[9.99, 45.0, 12.5]
    print(f"Task 4: Total={total}, Max={most_exp}, Reverse={reverse_cart}")

    # Task 5: User Management
    users = []

    def add_user(name):
        if name not in users: users.append(name)

    add_user("admin");
    add_user("student1");
    add_user("admin")  # Duplicate ignored
    users.sort()
    longest = max(users, key=len) if users else ""
    first_5 = users[:5]
    # Expected: users=['admin', 'student1'], longest='student1'
    print(f"Task 5: Sorted={users}, Longest={longest}, First 5={first_5}")

    # Task 6: Rock-Paper-Scissors (Round Logic)
    moves = ["paper", "rock", "scissors"]
    comp_move = random.choice(moves)
    user_move = "rock"  # Example move
    # Result depends on logic: rock beats scissors, paper beats rock
    print(f"Task 6: User={user_move}, Computer={comp_move}")


# ==========================================
# 2. FOR LOOPS
# ==========================================

def for_loop_exercises():
    print("\n=== 2. FOR LOOPS ===")

    # I-III: Counting
    print("I-III: 1 to 10:", [i for i in range(1, 11)])  # Expected: [1..10]
    print("Even 1-20:", [i for i in range(2, 21, 2)])  # Expected: [2, 4..20]

    # VI: Length without len()
    text = "Python"
    count = 0
    for _ in text: count += 1
    # Expected: 6
    print(f"VI: Count of '{text}' = {count}")

    # VIII: Sum of digits
    digits_text = "123abc45"
    d_sum = sum(int(c) for c in digits_text if c.isdigit())
    # Expected: 1+2+3+4+5 = 15
    print(f"VIII: Digit sum of '{digits_text}' = {d_sum}")

    # XIII: Multiplication table 1-5
    print("XIII: Multiplication Table 1-5:")
    for i in range(1, 6):
        print([i * j for j in range(1, 6)])

    # XXV: Inverted Triangle
    print("XXV: Inverted Triangle:")
    for i in range(5, 0, -1):
        print("*" * i)


# ==========================================
# 3. WHILE LOOPS
# ==========================================

def while_loop_exercises():
    print("\n=== 3. WHILE LOOPS ===")

    # IV: Prime check (Example: 7)
    n = 7
    i = 2
    is_prime = True
    while i < n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    else:
        # Expected: "7 is prime"
        print(f"IV: {n} is prime")

    # VI: Password with else
    attempts = 0
    success = False
    while attempts < 3:
        # Simulate correct entry on 2nd try
        if attempts == 1:
            success = True
            break
        attempts += 1
    if success:
        # Expected: Logged in
        print("VI: Logged in")


# ==========================================
# 4. LISTS
# ==========================================

def list_exercises():
    print("\n=== 4. LISTS ===")

    # IV: Count without len
    items = [3, 7, 2, 9, 4, 5]
    c = 0
    for _ in items: c += 1
    # Expected: 6
    print(f"IV: List size = {c}")

    # IX: Reverse in place
    lst = [1, 2, 3, 4, 5]
    lst.reverse()
    # Expected: [5, 4, 3, 2, 1]
    print(f"IX: Reversed: {lst}")

    # XII: Squares
    sq = [x ** 2 for x in [1, 2, 3, 4, 5]]
    # Expected: [1, 4, 9, 16, 25]
    print(f"XII: Squares: {sq}")

    # XXI: Join string
    joined = "".join(['A', 'B', 'C'])
    # Expected: "ABC"
    print(f"XXI: Joined: {joined}")


# ==========================================
# 5. SLICING
# ==========================================

def slicing_exercises():
    print("\n=== 5. SLICING ===")

    s_list = [i for i in range(1, 16)]  # 15 elements

    # IV: Reverse every 3rd
    # Expected: [15, 12, 9, 6, 3]
    print(f"IV: Rev every 3rd: {s_list[::-3]}")

    # VIII: All except first and last
    # Expected: [2, 3, ... 14]
    print(f"VIII: Middle: {s_list[1:-1]}")

    # X: Replace slice
    lst_x = [10, 20, 30, 40, 50, 60]
    lst_x[2:5] = [7, 8, 9]
    # Expected: [10, 20, 7, 8, 9, 60]
    print(f"X: Replaced slice: {lst_x}")

    # XV: Every second from end
    # Expected: [15, 13, 11, 9, 7, 5, 3, 1]
    print(f"XV: Every 2nd from end: {s_list[::-2]}")


if __name__ == "__main__":
    main_tasks()
    for_loop_exercises()
    while_loop_exercises()
    list_exercises()
    slicing_exercises()