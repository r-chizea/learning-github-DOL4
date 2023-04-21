"Linting practice."

def count(sequence, item):
    "A function that counts the amount of times a number appears in a sequence"

    counter = 0
    for number in sequence:
        if number == item:
            counter += 1
    return counter
