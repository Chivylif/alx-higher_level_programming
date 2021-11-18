#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_len = len(argv)
    index = 1
    if argv_len is 0:
        print("{:d} arguments.".format(argv_len))
    elif argv_len is 1:
        print("{:d} argument:".format(argv_len))
        print("{:d}: {:s}".format(index, sys.argv[index]))
    else:
        print("{:d} arguments:".format(argv_len))
        for index in range(1, argv_len + 1):
            print("{:d}: {:s}".format(index, sys.argv[index]))
