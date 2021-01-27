#!/usr/bin/python3
"""[Prints a text with 2 new lines after each of these characters]
"""


def text_indentation(text):
    """[summary]

    Args:
        text ([text]): [text to be printed]
    """
    new_text = ""
    salto = "\n\n"
    if type(text) != str:
        raise TypeError("text must be a string")

    for position in range(0, len(text)):
        if (text[position - 1] == "." or text[position - 1] == "?"
         or text[position - 1] == ":") and text[position] == " ":
            continue
        new_text += text[position]
        if text[position] == ":" or text[position] == "?" or text[position] == ".":
            new_text = new_text + salto

    print(new_text, end="")
