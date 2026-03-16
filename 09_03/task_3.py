import random

nums = [random.randint(1, 100) for _ in range(20)]
avg = sum(nums) / len(nums)

largest = max(nums)
smallest = min(nums)
greater_than_avg = sum(1 for x in nums if x > avg)
evens = [x for x in nums if x % 2 == 0]
every_second = nums[::2]

unique_nums = sorted(list(set(nums)))
second_largest = unique_nums[-2] if len(unique_nums) > 1 else None

print(f"Average: {avg}")
print(f"Max: {largest}, Min: {smallest}")
print(f"Numbers > Average: {greater_than_avg}")
print(f"Even numbers: {evens}")
print(f"Every second element: {every_second}")
print(f"Second largest: {second_largest}")
print("-" * 30)