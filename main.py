#!/bin/python3

import argparse
import sys

from rich import print

from caesar import bruteforce, decrypt, encrypt


def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Tool")

    parser.add_argument(
        "-e", "--encrypt", type=str, metavar="string", help="Text to encrypt"
    )
    parser.add_argument(
        "-d", "--decrypt", type=str, metavar="string", help="Text to decrypt"
    )
    parser.add_argument(
        "-b",
        "--bruteforce",
        type=str,
        metavar="string",
        help="Text to bruteforce decrypt",
    )

    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        default=0,
        help="Shift value for encryption/decryption",
    )

    args = parser.parse_args()

    if args.encrypt or args.decrypt:
        if args.shift <= 0:
            print(
                "[bold red]Shift value must be a positive integer for encryption![/bold red]"
            )
            sys.exit(1)

    if args.encrypt:
        encrypted_text = encrypt(args.encrypt, args.shift)
        if encrypted_text is not None:
            print(f"Encrypted Text: [bold green]{encrypted_text}[/bold green]")

    elif args.decrypt:
        decrypted_text = decrypt(args.decrypt, args.shift)
        if decrypted_text is not None:
            print(f"Decrypted Text: [bold green]{decrypted_text}[/bold green]")

    elif args.bruteforce:
        bruteforce(args.bruteforce)


if __name__ == "__main__":
    main()
