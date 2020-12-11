#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lista = dir(hidden_4)
    for palabra in lista:
        if palabra[0] is not "_":
            print("{}".format(palabra))
