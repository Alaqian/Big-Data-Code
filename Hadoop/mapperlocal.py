#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys


def read_input(input):
    for line in input:
        # split the line into words; keep returning each word - for each line in the input, return each line
        yield line.split()


def main(
    separator="\t",
):  # default separator is a tab - which is \t - can change it to something else
    # input comes from STDIN (standard input) - read and input from standard input
    data = read_input("The cat in the hat is teh best cat in the hat.")

    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in line:
            print("%s%s%d" % (word, separator, 1))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
