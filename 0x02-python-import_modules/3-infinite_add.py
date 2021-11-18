#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    len = len(sys.argv) - 1
    index = 1
    while index <= len:
        total_sum += int(sys.argv[index])
        index++
    print("{:d}".format(total_sum))
