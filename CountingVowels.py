vowels = "AEIOUaeiou"
counter = 0
sentence = input("please enter a sentence: ")
for letter in sentence:
    if letter in vowels:
        counter += 1

print(counter)
