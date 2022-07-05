#!/usr/bin/python3

import random
import argparse
import string

parser = argparse.ArgumentParser(description="Generate a random password")

parser.add_argument("-l",
                    "--length",
                    type=int,
                    default=8,
                    help="Length of password")

parser.add_argument("-u",
                    "--upper",
                    default=False,
                    action="store_true",
                    help="Include uppercase letters")

parser.add_argument("-d",
                    "--digit",
                    default=False,
                    action="store_true",
                    help="Include digits")

parser.add_argument("-p",
                    "--punctuation",
                    default=False,
                    action="store_true",
                    help="Include pupnctuation ")

args = parser.parse_args()


def generate_password(length, upper, digit, punctuation):
    """
    Generate a random password
    """
    chars = ""

    if upper:
        chars += string.ascii_uppercase
    if digit:
        chars += string.digits
    if punctuation:
        chars += string.punctuation

    chars += string.ascii_lowercase

    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == '__main__':

    print(
        generate_password(args.length, args.upper, args.digit,
                          args.punctuation))
    exit(0)