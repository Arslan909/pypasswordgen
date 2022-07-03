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

args = parser.parse_args()


def generate_password(length):
    """
    Generate a random password
    """
    password = "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length))
    return password


if __name__ == "__main__":
    print(generate_password(args.length))
    exit(0)
