#!/usr/bin/python3
"""[function that returns an object (Python data structure)]"""


def from_json_string(my_str):
    """[function that returns an object (Python data structure)]"""
    import json
    data = json.loads(my_str)
    return data
