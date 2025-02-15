lst = [1, 2, 3, 4, 5, 6]

if len(lst) == 0:
    result = [[], []]
elif len(lst) % 2 == 0:
    mid = len(lst) // 2
    result = [lst[:mid], lst[mid:]]
else:
    mid = len(lst) // 2 + 1
    result = [lst[:mid], lst[mid:]]

print(result)
