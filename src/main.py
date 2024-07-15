#!/usr/bin/python

import re

def returnMatches(f: str, myRE: str, n_lines = 1):
	"""
    Print matching lines, and number of subsequent lines.
    :param n_lines: number of lines to print after the matching line.  1 means to print only the matching line.
        :return: the lines in a list or None after printing them.
    """
	# lines = open(f).readlines()
	# myFile = open(f)
	flag = False
	with open(f) as myFile:
		for currentLineMatch, line in enumerate(myFile):
			# print(num, line)
			if flag:
				nlines -= 1
				print(line)
			regex = re.search(myRE, line)
			# print(regex)
			if regex is not None:
				print(line.strip())
				flag = True
				# for i in range(nlines - 1):
				# 	print(lines[currentLineMatch+i+1].strip())

returnMatches("../var/sample.in", "better than never")
