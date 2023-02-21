#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator="\t"):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split("\t")


def main(separator="\t"):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby   groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for key, group in groupby(data, itemgetter(0)):
        # dangerous, could run out of memory, loads everything at once.
        try:
            w1 = ""
            w2 = ""
            for key, value in group:
                w1 = key
                value = value.split()
                if len(value) == 1:
                    pw1 = int(value[0])
                else:
                    pw1nw2 = int(value[-1])
                    w2 = str(value[-2])
            pw2gw1 = pw1nw2 / pw1
            print("%s%s%d" % ("P(" + w1 + "|" + w2 + ")", "\t", pw2gw1))
        except ValueError:
            # count was not a number, so silently discard this item
            pass


if __name__ == "__main__":
    main()
