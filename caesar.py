#!/bin/python3

import string

from rich import print

UPPER_CASE = string.ascii_uppercase
LOWER_CASE = string.ascii_lowercase
NUMBERS_SYMBOLS = string.digits + string.punctuation + string.whitespace

# chift characters using the value of shift
def shift_char(char, shift, alphabet):
    shifted_index = (alphabet.index(char) + shift) % len(alphabet)
    return alphabet[shifted_index]

# encrypt text Input
def encrypt(text, shift=0):
    encrypted = ""
    for char in text:
        if char in UPPER_CASE:
            encrypted += shift_char(char, shift, UPPER_CASE)

        elif char in LOWER_CASE:
            encrypted += shift_char(char, shift, LOWER_CASE)

        elif char in NUMBERS_SYMBOLS:
            encrypted += char

        else:
            print("[bold red]Input contains a non-printable character![/bold red]")
            return None
    return encrypted

# decrypt text Input
def decrypt(text, shift=0):
    decrypted = ""
    for char in text:
        if char in UPPER_CASE:
            decrypted += shift_char(char, -shift, UPPER_CASE)

        elif char in LOWER_CASE:
            decrypted += shift_char(char, -shift, LOWER_CASE)

        elif char in NUMBERS_SYMBOLS:
            decrypted += char

        else:
            print("[bold red]Input contains a non-printable character![/bold red]")
    return decrypted

# bruteforce decrypted text
def bruteforce(text):
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        print(
            f"Deciphered with shift [bold green]{shift}[/bold green]: [bold green]{decrypted}[/bold green]"
        )
