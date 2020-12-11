#!/usr/bin/python3
import sys
if __name__ == '__main__':
    m = len((sys.argv))

    if m - 1 == 0:
        print("{} arguments.".format(m-1))
    elif m - 1 == 1:
        print("{} argument:".format(m-1))
        print("{}: {}".format(m-1, str(sys.argv[1])))
    elif m - 1 > 1:
        print("{} arguments:".format(m-1))
        for i in range(1, (len(sys.argv))):
            print("{}: {}".format(i, str(sys.argv[i])))
