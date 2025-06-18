vowel = ['a','e','i','o','u']
word = input('What word would you like to seatch for?? ')
count = 0
for character in word:
    if character in vowel:
        count +=1
print(count)