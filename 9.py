import string, keyword

name = input("Enter the variable name: ")

print(
    name not in keyword.kwlist
    and name.count('_') <= 1
    and not name[0].isdigit()
    and not any(c.isupper() for c in name)
    and all(c.isalnum() or c == '_' for c in name)
)
