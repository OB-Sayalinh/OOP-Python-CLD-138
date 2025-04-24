user_word = input("Please enter a word: ")

# What I find funny about this is that using the continue
# Statement is rather useless from the given parameters

for letter in user_word:
    if letter.lower() not in "aeiou":
        print(letter.upper())
    else:
        continue

# I now realize I am supposed to loop through each vowel
# In elif statements which is why we need continue
#
# for letter in user_word:
#     lower_letter = letter.lower()
#     if lower_letter in "a":
#         continue
#     elif lower_letter in "e":
#       continue
#     elif lower_letter in "i":
#       continue
#     elif lower_letter in "o":
#        continue
#     elif lower_letter in "u":
#        continue
#     else:
#         print(letter.upper())
