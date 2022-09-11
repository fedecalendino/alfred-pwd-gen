import sys

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


def make_subtitle(length, strength):
    strength = min(int(len(STRENGTH_BAR) * strength), len(STRENGTH_BAR))

    return "{bar_colors}{bar_filler} | length: {length}".format(
        bar_colors=STRENGTH_BAR[:strength],
        bar_filler=STRENGTH_BAR_FILLER * (len(STRENGTH_BAR) - strength),
        length=length,
    )


def select_icon(strength):
    strength = min(int(len(STRENGTH_BAR) * strength), len(STRENGTH_BAR))
    color = STRENGTH_BAR[strength - 1]

    return f"img/icons/{ICONS[color]}.png"


def make_mod_subtitle(letters, digits, symbols):
    def format_number(value: int, name: str) -> str:
        return f"{value} {name}" + ("s", "")[value == 1]

    return "{length} characters = {letters}, {digits} and {symbols}".format(
        length=letters + digits + symbols,
        letters=format_number(letters, "letter"),
        digits=format_number(digits, "digit"),
        symbols=format_number(symbols, "symbol"),
    )


def parse_args(args):
    values = [15, 5, 5]

    try:
        for i, value in enumerate(args):
            values[i] = int(value.strip())
    except:
        pass

    return values


def main(workflow):
    letters, digits, symbols = parse_args(workflow.args)

    for _ in range(5):
        password = generator.generate(letters, digits, symbols)
        strength = generator.strength(password)

        workflow.new_item(
            title=" {}".format(password),
            subtitle=make_subtitle(
                length=letters + digits + symbols,
                strength=strength,
            ),
            arg=password,
            copytext=password,
            valid=True,
        ).set_icon_file(path=select_icon(strength),).set_alt_mod(
            arg=password,
            subtitle=make_mod_subtitle(letters, digits, symbols),
        ).set_cmd_mod(
            arg=password,
            subtitle=make_mod_subtitle(letters, digits, symbols),
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
