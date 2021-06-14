def letter_count(a_string):
    letters = 0
    for character in a_string:
        if not character == " ":
            letters += 1
    return letters


def word_count(a_string):
    words = 1
    for character in a_string:
        if character == " ":
            words += 1
    return words


def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)

  
  a_string = "Up with the white and gold"

print(average_word_length(a_string))
