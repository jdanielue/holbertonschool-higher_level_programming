#!/usr/bin/python3
""" script that adds all arguments to a Python list"""


import json
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

new_list = []
if len(sys.argv) == 1 :
    save_to_json_file(new_list, "add_item.json")
else :
    new_list = load_from_json_file("add_item.json")
    new_list = new_list + sys.argv[1:]
    save_to_json_file(new_list, "add_item.json")

"""[teoria 1]
crear una lista
si no hay argumentos imprimir la lista vacia
de lo contrario llenar la lista

"""
