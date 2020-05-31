# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.


def reverse(long_string):

    string_list = long_string.split()
    new_string = string_list[::-1]
    joined_new_string = " ".join(new_string)
    print(joined_new_string)


reverse(input("Enter a sentence: "))
