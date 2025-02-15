examples = [
    [0, 1, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [0, 2, 4, 0, 15, 26, 0, 0, 26],
    []
]

for lst in examples:
    non_zero = [x for x in lst if x != 0]
    zeros = [x for x in lst if x == 0]
    result = non_zero + zeros
    print(f"{lst} -> {result}")
