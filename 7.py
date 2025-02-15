examples = [
    [12, 2, 4, 0, 5],
    [1, 4, 0, 0],
    [0],
    [2, 4, 4],
    [],
]

for lst in examples:
    if not lst:
        result = 0
    else:
        even_index_sum = sum(lst[i] for i in range(0, len(lst), 2))
        result = even_index_sum * lst[-1]
    print(f"{lst} -> {result}")
