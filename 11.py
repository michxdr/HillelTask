import string

input_string = input("Enter a string: ")

cleaned_words = [''.join(e for e in word if e not in string.punctuation) for word in input_string.split()]
hashtag = '#' + ''.join(word.capitalize() for word in cleaned_words if word)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print("Generated hashtag:", hashtag)
