def task_5():
    names = ["John", "Mary", "Kitty", "Alice", "John", "Mary", "Al", "Bill", "John", "Alice", "Al"]

    lengths = [len(n) for n in names]
    print(lengths)

    len_to_list = {}
    len_to_set = {}
    name_counts = {}

    for name in names:
        l = len(name)
        # Populate length to list
        if l not in len_to_list:
            len_to_list[l] = []
        len_to_list[l].append(name)

        # Populate length to set
        if l not in len_to_set:
            len_to_set[l] = set()
        len_to_set[l].add(name)

        # Populate name counts
        name_counts[name] = name_counts.get(name, 0) + 1

    print(len_to_list)
    print(len_to_set)
    print(name_counts)

task_5()