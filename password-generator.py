"""
Generate a random password with a specified minimum length.

Parameters:
- min_length (int): The minimum length of the generated password.
- numbers (bool, optional): If True, include digits in the password. Default is True.
- special_characters (bool, optional): If True, include special characters in the password. Default is True.

Returns:
- str: A random password with the specified minimum length and optional characters.
"""

import random 
import string


def generate_password(min_length, numbers=True, special_characters=True):
    """
    Generate a random password with a specified minimum length.

    Parameters:
    - min_length (int): The minimum length of the generated password.
    - numbers (bool, optional): If True, include digits in the password. Default is True.
    - special_characters (bool, optional): If True, include special characters in the password. Default is True.

    Returns:
    - str: A random password with the specified minimum length and optional characters.
    """
    letters = string.ascii_letters 
    digits = string.digits
    special = string.punctuation

    characters = letters 
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ''.join(random.choice(characters) for _ in range(min_length))
    return password

# Input the number of characters within your password.
print(generate_password(10))