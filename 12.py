import string

all_letters = string.ascii_letters

letter_range = input("Enter the letter range (e.g., a-c): ")

start_letter, end_letter = letter_range.split('-')

start_index = all_letters.index(start_letter)
end_index = all_letters.index(end_letter)

result = all_letters[start_index:end_index + 1]

print(result)
