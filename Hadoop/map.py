import sys
import re

for line in sys.stdin:
    line = re.sub("[^a-zA-Z0-9]", " ", line.lower())
    words = line.split()
    for word in words:
        print("%s%s%d" % (word, "\t", 1))
