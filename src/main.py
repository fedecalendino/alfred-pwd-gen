import sys
from typing import List

from pyflow import Workflow

import generator

ICONS = {
    "⬛": "black",
    "🟫": "brown",
    "🟥": "red",
    "🟧": "orange",
    "🟨": "yellow",
    "🟩": "green",
    "🟦": "blue",
    "🟪": "purple",
}


STRENGTH_BAR = "⬛⬛⬛🟫🟫🟫🟥🟥🟥🟧🟧🟧🟨🟨🟨🟩🟩🟩🟦🟦🟦🟪🟪🟪"
STRENGTH_BAR_FILLER = "⬜"


def make_subtitle(length: int, strength: int):
    strength = min(
        int(len(STRENGTH_BAR) * strength),
        len(STRENGTH_BAR),
    )

    return "{bar_colors}{bar_filler} | length: {length}".format(
        bar_colors=STRENGTH_BAR[:strength],
        bar_filler=STRENGTH_BAR_FILLER * (len(STRENGTH_BAR) - strength),
        length=length,
    )


def select_icon(strength: int):
    strength = min(
        int(len(STRENGTH_BAR) * strength),
        len(STRENGTH_BAR),
    )

    color = STRENGTH_BAR[strength - 1]

    return f"img/icons/{ICONS[color]}.png"


def make_mod_subtitle(letters: int, digits: int, symbols: int):
    def format_number(value: int, name: str) -> str:
        return f"{value} {name}" + ("s", "")[value == 1]

    return "{length} characters = {letters}, {digits} and {symbols}".format(
        length=letters + digits + symbols,
        letters=format_number(letters, "letter"),
        digits=format_number(digits, "digit"),
        symbols=format_number(symbols, "symbol"),
    )


def parse_args(args: List[str]):
    values = [15, 6, 6]

    try:
        for i, value in enumerate(args):
            values[i] = int(value.strip())
    except:
        pass

    return values


def increment(value: int, inc: int) -> int:
    if value == 0:
        return 0

    return value + inc


def main(workflow: Workflow):
    letters, digits, symbols = parse_args(workflow.args)

    for x in [0, 0, -2, -1, 1, 2]:
        l = increment(letters, x)
        d = increment(digits, x)
        s = increment(symbols, x)

        password = generator.generate(l, d, s)
        strength = generator.strength(password)

        workflow.new_item(
            title=" {}".format(password),
            subtitle=make_subtitle(
                length=l + d + s,
                strength=strength,
            ),
            arg=password,
            copytext=password,
            valid=True,
        ).set_icon_file(
            path=select_icon(strength),
        ).set_alt_mod(
            arg=password,
            subtitle=make_mod_subtitle(l, d, s),
        ).set_cmd_mod(
            arg=password,
            subtitle=make_mod_subtitle(l, d, s),
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
