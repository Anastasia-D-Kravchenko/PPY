users = ["Anna", "Zack", "Marta"]

def add_user(list_ref, name):
    if name not in list_ref:
        list_ref.append(name)
    else:
        print(f"Duplicate prevented: {name}")


add_user(users, "Kamil")
add_user(users, "Anna")

users.sort()
first_5 = users[:2]
longest = max(users, key=len)

print(f"Alphabetical list: {users}")
print(f"First 5: {first_5}")
print(f"Longest username: {longest}")
print("-" * 30)