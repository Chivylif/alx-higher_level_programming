#!/usr/bin/python3
# a program that prints the ASCII alphabet, in lowercase, not followed by a new line except 'e' and 'q'
for i in range(97, 123):
	if i == 101 or i == 113:
		continue
	else:
		print("{:s}".format(chr(i)), end='')
