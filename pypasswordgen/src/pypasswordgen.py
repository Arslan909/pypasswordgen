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
                    action="count",
                    help="Include uppercase letters")

parser.add_argument("-d",
                    "--digit",
                    default=False,
                    action="count",
                    help="Include digits")

parser.add_argument("-p",
                    "--punctuation",
                    default=False,
                    action="count",
                    help="Include pupnctuation ")

args = parser.parse_args()


def generate_password(length, upper, digit, punctuation):
    """
    Generate a random password
    """
    chars = ""
    if upper == 2:
        chars += string.ascii_uppercase
        return ''.join(random.choice(chars) for _ in range(length))

    if digit == 2:
        chars += string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    if punctuation == 2:
        chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

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
