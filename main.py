# coding=utf-8

import sys

from workflow import Workflow

import generator


def parse_args(args):
    values = [10, 5, 5]

    try:
        for i, value in enumerate(args):
            values[i] = int(value.strip())
    except:
        pass

    return values


def format_subtitle(letters, digits, symbols, streght):
    letters = "{} letter{}".format(letters, "" if letters == 1 else "s")
    digits = "{} digit{}".format(digits, "" if digits == 1 else "s")
    symbols = "{} symbol{}".format(symbols, "" if symbols == 1 else "s")

    if streght == 0:
        streght = 1
        symbol = u"\U00002B1B"  # Black Square
    elif streght < 4:
        symbol = u"\U0001F7E5"  # Red Square
    elif streght < 7:
        symbol = u"\U0001F7E8"  # Yellow Square
    elif streght < 12:
        symbol = u"\U0001F7E9"  # Green Square
    elif streght < 15:
        symbol = u"\U0001F7E9"  # Green Square
    else:
        symbol = u"\U0001F7E6"  # Blue Square

    return u" {} | {} | {} | {}".format(symbol * streght, letters, digits, symbols)


def main(workflow):
    letters, digits, symbols = parse_args(workflow.args)

    for _ in range(5):
        password = generator.generate(letters, digits, symbols)
        streght = generator.streght(password)

        workflow.add_item(
            title=" {}".format(password),
            subtitle=format_subtitle(letters, digits, symbols, streght),
            arg=password,
            copytext=password,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
