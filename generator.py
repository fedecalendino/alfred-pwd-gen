import random

from math import log


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!#$%&*+,-.:;<=>?@^_`~|"


def generate(letters, digits, symbols):
    characters = []

    for amount, space in [(letters, LETTERS), (digits, DIGITS), (symbols, SYMBOLS)]:
        tmp = (random.choice(space) for _ in range(amount))
        characters.extend(tmp)

    random.shuffle(characters)

    return ''.join(characters)


def _calc_streght(password):
    return len(password) * log(len(set(password)), 2)


def streght(password):
    if not password:
        return 0

    current = _calc_streght(password)
    baseline = _calc_streght(generate(9, 5, 5))

    if current > baseline:
        return 16

    return int(15 * current/baseline)
