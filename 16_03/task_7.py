def task_7():
    dct = {'John': 3, 'Bill': 4, 'Jane': 4, 'Kim': 2, 'Mary': 3, 'Joe': 0, 'Sue': 5, 'Ada': 2, 'Ray': 2}

    wins_to_players = {}
    for player, wins in dct.items():
        if wins not in wins_to_players:
            wins_to_players[wins] = []
        wins_to_players[wins].append(player)

    print("Dictionary (wins -> players):")
    print(wins_to_players)

    # Create list of tuples and sort descending by wins
    sorted_tuples = sorted(wins_to_players.items(), key=lambda item: item[0], reverse=True)

    print("\nSorted list of tuples (descending by wins):")
    print(sorted_tuples)

task_7()