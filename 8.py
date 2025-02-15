import random

examples = [
    [random.randint(1, 100) for _ in range(random.randint(3, 10))]
]

for lst in examples:
    if len(lst) < 3:
        result = []
    else:
        result = [lst[0], lst[2], lst[-2]]
    print(f"{lst} -> {result}")
