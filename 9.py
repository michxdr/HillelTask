import string, keyword

name = input("Enter the variable name: ")

is_valid = (
    name not in keyword.kwlist
    and not name[0].isdigit()
    and not any(c.isupper() for c in name)
    and all(c.isalnum() or c == '_' for c in name)
    and "__" not in name
)

print(is_valid)
