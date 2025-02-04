lst = [1, 2]

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)

lst = []

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)

lst = [13, 5, 4, 0]

if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]

print(lst)



