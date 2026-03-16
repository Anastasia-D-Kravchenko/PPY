def task_6():
    N = int(input("Enter the number of distinct elements (N): "))
    distinct = set()
    all_numbers = []

    while len(distinct) < N:
        try:
            num = int(input("Enter a number: "))
            all_numbers.append(num)
            distinct.add(num)
        except ValueError:
            print("Please enter a valid integer.")

    duplicates = set([x for x in all_numbers if all_numbers.count(x) > 1])

    print(f"All distinct numbers: {distinct}")
    print(f"Numbers entered more than once: {duplicates}")

task_6()