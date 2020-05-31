# Code a random password generator in Python.
# Ask the user how strong they want their password to be.


import random
import string


def password_generator(strength):
    symbols_list = ["!", "@", "#", "%", "&", "*"]

    if strength == "strong":
        length = 9
    elif strength == "weak":
        length = 6
    else:
        print("Please type either 'strong' or 'weak'.")

    password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase +
                                      string.digits + "".join(symbols_list), k=length))
    print(password)


try:
    password_generator(input("Do you want a strong or weak password? Type 'strong' or 'weak': ").lower())
except UnboundLocalError:
    print("Please restart the programme.")
