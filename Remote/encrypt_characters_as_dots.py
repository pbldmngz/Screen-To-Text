CHARACTER_LIST = [
    "",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    " ",
    ".",
    ",",
    "!",
    "?",
    ":",
    ";",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "-",
    "_",
    "+",
    "=",
    "/",
    "\\",
    "|",
    "`",
    "~",
    "'",
    '"',
    "鳳",  # uses for characters that repeat themselves
    "端",  # End of page,
    "á",
    "é",
    "í",
    "ó",
    "ú",
    "Á",
    "É",
    "Í",
    "Ó",
    "Ú",
    "ñ",
    "Ñ",
    "¿",
    "¡",
    "ä",
    "Ä",
    "ë",
    "Ë",
    "ï",
    "Ï",
    "ö",
    "Ö",
    "ü",
    "Ü",
]


def get_character_map():
    symbol_dictionary = {}

    for idx, symbol in enumerate(CHARACTER_LIST):
        symbol_dictionary[symbol] = idx

    return symbol_dictionary


def encrypt_character(dot_number):
    max_columns = 14
    dot_spacing = "  "
    dot_symbol = "*"

    padding_top = "\n" * 5
    padding_left = " " * 10

    output_text = "" + padding_top

    amount_of_rows = dot_number // max_columns
    amount_of_elements_last_row = dot_number % max_columns

    output_text += (
        f"{padding_left}{(dot_symbol + dot_spacing) * max_columns}\n\n" * amount_of_rows
    )
    output_text += (
        f"{padding_left}{(dot_symbol + dot_spacing) * amount_of_elements_last_row}"
    )

    return output_text
