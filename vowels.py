def count_vowels(sentence):
    vowels = "AEIOUaeiou"
    counter = 0

    for letter in sentence:
        if letter in vowels:
            counter += 1

    return(counter)
