# --- PPY SURPRISE EXAM PREP (PART 2): LISTS, SLICING, & ADVANCED LOOPS ---
# Based on PPY02ang.pdf: Emphasizing mutability, ASCII math, and loop control.

# 1. THE WHILE...ELSE / FOR...ELSE TRAP
# Trick: 'else' executes only if 'break' is NOT hit. [cite: 518, 519, 971, 972]
print("--- 1. Loop...Else Trap ---")


def check_all_positive():
    for i in range(5):
        num = int(input(f"({i + 1}/5) Enter a number: "))  # input() returns str [cite: 147]
        if num < 0:
            print("Negative number detected! Breaking loop.")
            break  # Loop terminates early
    else:
        # Runs ONLY if the loop finishes naturally (all iterations complete)
        print("All numbers were positive!")


# check_all_positive() # Uncomment to test


# 2. MODIFYING A LIST WHILE ITERATING
# Trick: Use slicing [:] to iterate over a COPY to avoid skipping items. [cite: 609, 610, 1026, 1027]
def remove_evens(lst):
    # Removing items shifts indices. Iterating over the original 'lst' would fail.
    for x in lst[:]:  # [:] creates a copy for safe iteration [cite: 588, 610]
        if x % 2 == 0:
            lst.remove(x)  # Modifies original 'lst' in-place [cite: 547, 985]


my_list = [1, 2, 2, 3, 4, 4, 5]
remove_evens(my_list)
print(f"2. Evens removed (In-place): {my_list}")  # Expected: [1, 3, 5]


# 3. ASCII MATH WITH ORD() AND CHR()
# Trick: Lowercase to Uppercase = ASCII code - 32. [cite: 627, 629, 632]
def custom_upper(text):
    # ord() gets ASCII integer, chr() returns character [cite: 627, 629]
    # 'a' (97) - 32 = 'A' (65). Logic applies to all 'a'-'z'. [cite: 632]
    chars = [chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in text]
    return "".join(chars)  # Joins list of chars into one string [cite: 432]


print(f"3. Custom Upper: {custom_upper('Hello World! 123')}")

# 4. ADVANCED SLICE ASSIGNMENT
# Trick: Replace chunks of a list in one line. [cite: 590, 1028, 1029]
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Replace first 3 [:3] with last 3 [-3:] in reverse order [::-1] [cite: 574, 579, 582]
numbers[:3] = numbers[-3:][::-1]

print(f"4. Slice Assignment result: {numbers}")


# 5. TRACKING CONSECUTIVE STATES (2-LOSSES RULE)
# Trick: Reset or increment a counter based on round outcomes. [cite: 320, 321]
def check_game_over(results):
    consecutive_losses = 0
    for result in results:
        if result == 'loss':
            consecutive_losses += 1
        else:
            consecutive_losses = 0  # RESET counter on win/draw

        if consecutive_losses == 2:
            return "Game Over: 2 losses in a row!"
    return "Game finished normally."


results_list = ['win', 'loss', 'draw', 'loss', 'loss', 'win']
print(f"5. State Tracking: {check_game_over(results_list)}")


# 6. PRIME NUMBERS + LIST COMPREHENSIONS
# Trick: Check for divisors from 2 to n-1. [cite: 643, 644, 649, 650]
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):  # range(2, n) excludes 1 and n [cite: 649]
        if n % i == 0:  # If divisible, not prime [cite: 650]
            return False
    return True


# Comprehension with a condition [cite: 560, 561, 1002, 1003]
primes = [x for x in range(2, 51) if is_prime(x)]
print(f"6. Primes (2-50): {primes}")

# --- KEY SURVIVAL TIPS ---
# - Mutability: 'b = a' makes 'b' point to 'a'. Changes in 'b' affect 'a'. [cite: 605, 606, 607, 608]
# - In-place: 'list.sort()' changes the original. 'sorted(list)' returns a NEW one. [cite: 1118, 1119, 1124, 1125]
# - Slicing: [start:stop:step]. 'stop' index is NEVER included. [cite: 567, 570, 1009, 1011]