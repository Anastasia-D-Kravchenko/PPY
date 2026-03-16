import random


def task_3():
    moves_dict = {"paper": 1, "rock": 2, "scissors": 3}
    history = []
    stats = {"wins": 0, "losses": 0, "draws": 0}

    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")
        user_input = input("Enter rock, paper, or scissors: ").lower()

        if user_input not in moves_dict:
            print("Invalid move, skipping round.")
            continue

        comp_input = random.choice(list(moves_dict.keys()))
        print(f"Computer chose: {comp_input}")

        u_val = moves_dict[user_input]
        c_val = moves_dict[comp_input]

        # Determine winner: 1 beats 2 (paper beats rock), 2 beats 3 (rock beats scissors), 3 beats 1 (scissors beats paper)
        if u_val == c_val:
            result = "draw"
            stats["draws"] += 1
        elif (u_val == 1 and c_val == 2) or (u_val == 2 and c_val == 3) or (u_val == 3 and c_val == 1):
            result = "win"
            stats["wins"] += 1
        else:
            result = "loss"
            stats["losses"] += 1

        print(f"Result: {result}")
        history.append((user_input, comp_input, result))

    print("\n=== Game Summary ===")
    print(f"History: {history}")
    print(f"Stats: {stats}")

task_3()