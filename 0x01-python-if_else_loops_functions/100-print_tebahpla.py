#!/usr/bin/python3
for letras, LETRAS in zip(range(122, 96, -2), range(89, 55, -2)):
    print("{:c}{:c}".format(letras, LETRAS), end="")
