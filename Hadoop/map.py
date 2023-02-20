import sys
import re

for line in sys.stdin:
    line = re.sub("[^a-zA-Z0-9]", " ", line.lower())
    words = line.split()
    words_in_line = len(words)
    for i in range(words_in_line):
        print("%s%s%d" % (words[i], "\t", 1))
        if i < words_in_line - 1:
        print("%s%s%d" % (words[i] + " " + words[i + 1], "\t", 1))"""
        if i < words_in_line - 2:
            print("%s%s%d" % (words[i] + " " + words[i + 1] + " " + words[i + 2], "\t", 1))
