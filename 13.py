seconds = int(input("Enter the number of seconds: "))

days, seconds_left = divmod(seconds, 24 * 60 * 60)
hours, seconds_left = divmod(seconds_left, 60 * 60)
minutes, seconds = divmod(seconds_left, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

result = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

print(result)
