def is_even(num):
    return num % 2 == 0


def is_greater_than_10(num):
    return num > 10


def filter_list(lst, predicate):
    return [x for x in lst if predicate(x)]


def task_4():
    N = int(input("Enter N: "))
    # Start at 2 (not 0), step is 3 (not 1)
    lst = list(range(2, 2 + N * 3, 3))
    print(f"Generated list: {lst}")

    # Using predefined predicate
    even_list = [x for x in lst if is_even(x)]
    print(f"Filtered (even numbers): {even_list}")

    # Testing custom function
    print(f"Custom filter (greater than 10): {filter_list(lst, is_greater_than_10)}")

task_4()