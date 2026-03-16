import random

options = ["paper", "rock", "scissors"]
u_moves, c_moves = [], []
wins, losses, draws = 0, 0, 0

for _ in range(3):
    comp = random.choice(options)
    user = random.choice(options)

    u_moves.append(user)
    c_moves.append(comp)

    if user == comp:
        draws += 1
    elif (user == "rock" and comp == "scissors") or \
            (user == "paper" and comp == "rock") or \
            (user == "scissors" and comp == "paper"):
        wins += 1
    else:
        losses += 1

    if len(u_moves) >= 2:
        pass

print(f"User moves: {u_moves}")
print(f"Computer moves: {c_moves}")
print(f"Results: Wins={wins}, Losses={losses}, Draws={draws}")
print("-" * 30)