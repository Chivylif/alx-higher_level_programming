#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0
    len = len(sys.argv) - 1
    for x in range(len):
        total_sum += int(sys.argv[x + 1])
    print("{:d}".format(total_sum))
