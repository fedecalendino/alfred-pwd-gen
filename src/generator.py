import random
import secrets
from math import log

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!#$%&*+,-.:;<=>?@^_`~|"


def generate(letters: int, digits: int, symbols: int):
    characters = []

    for amount, space in [(letters, LETTERS), (digits, DIGITS), (symbols, SYMBOLS)]:
        tmp = (secrets.choice(space) for _ in range(amount))
        characters.extend(tmp)

    random.shuffle(characters)

    return "".join(characters)


def calc(password: str):
    return int(len(password) * log(len(set(password)), 2))


def strength(password: str):
    if not password:
        return 0

    current = calc(password)
    baseline = calc(generate(15, 5, 5))

    return current / baseline
