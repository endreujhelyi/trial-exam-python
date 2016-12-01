# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

import os

def letter_counter(file_name):
    letter = 'a'
    sum_letter = 0
    if not os.path.isfile(file_name):
        return 0
    else:
        text = open(file_name)
        for line in text:
            for character in line:
                if character == letter:
                    sum_letter += 1
        text.close()
    return sum_letter
