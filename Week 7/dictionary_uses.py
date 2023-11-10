#  Darren showed how dictionaries are useful as data structures
import random

nums = []

for i in range(100000):
    nums.append(random.randint(1, 100))


counts = {}

for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

print(counts)
