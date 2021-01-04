#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' for object of")
        sys.stderr.write(" type 'str' Holberton is not an integer\n")
        return False
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' for object of")
        sys.stderr.write(" type 'str' Holberton is not an integer\n")
        return False
    else:
        return True
