word_without_vowels = ""

user_word = input("Please enter a word: ")

# Great! A use for the else statement

for letter in user_word:
    if letter.lower() not in "aeiou":
        print(letter.upper())
    else:
        word_without_vowels += letter.lower()
        continue

print(word_without_vowels)