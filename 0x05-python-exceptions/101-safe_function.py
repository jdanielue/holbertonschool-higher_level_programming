#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        
        return *fct
    except exception as urrego:
        sys.stderr.write("Exception:\n".format(urrego))
        return False