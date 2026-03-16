def task_2():
    users = set()

    while True:
        name = input("Enter a new user name (or 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        users.add(name)

    check_name = input("Enter a name to check if it exists: ")
    if check_name in users:
        print(f"{check_name} is in the set.")
    else:
        print(f"{check_name} is not in the set.")

    sorted_users = sorted(list(users))
    print(f"\nAlphabetical order: {sorted_users}")
    print(f"Number of unique users: {len(users)}")

    if len(sorted_users) >= 3:
        first_three = tuple(sorted_users[:3])
        print(f"First three users (tuple): {first_three}")

    if users:
        longest_name = max(users, key=len)
        print(f"User with the longest name: {longest_name}")

    user1 = input("Enter first.py user to check: ")
    user2 = input("Enter second user to check: ")
    print(f"Do both exist? {user1 in users and user2 in users}")

    print(f"Selected portion (first.py 2 users): {sorted_users[:2]}")

task_2()