# INFO
# Version meant as algorithm and efficiency tester for just alphabets in the password
# To extend functoinality to alphanumeric and special characters as well, change the list
# variable 'bits' to whatever characters you think the password can have.

# ANOTHER APPROACH
# Use of ASCII values can be made in algorithm to allow for global and a 100% surity in cracking,
# except for the fact that its gonna take quite long.

# EXTENSION
# Threading can be used for better performance:
#   : either in the current algorithm
#   : or in a hybrid of both algorithms (custom-list VS ASCII)


# CODE

# from os import system as cmd
# from time import sleep

PASSWORD = 'mysecretpassword'

bits = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',]



def generate(n):
    # generates a password of 'n' characters.
    # Can either generate a MASSIVE list of all possibilities and return it to check.
    # OR it can return one-password of 'n'-length at a call.
    return 0

print('Starting brute force attack...')
PSWD_LENGTH = int(input('Length of password (at most): '))


for length in range(1, PSWD_LENGTH+1):
    pass
