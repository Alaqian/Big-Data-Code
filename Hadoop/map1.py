#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import re
import sys


def read_input(input):
    for line in input:
        # Apply regex to replace undesired characters and lower case input
        line = re.sub("[^a-zA-Z0-9]", " ", line.lower())
        # split the line into words; keep returning each word - for each line in the input, return each line
        yield line.split()


def main(separator="\t"):
    # default separator is a tab - which is \t - can change it to something else
    # input comes from STDIN (standard input) - read and input from standard input
    line = read_input(sys.stdin)
    for words in line:
        words_in_line = len(words)  # Count the number of words in the line
        if words_in_line < 3:  # check if there are atleast 3 words in the line
            break
        for i in range(words_in_line):
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
            #
            # tab-delimited; the trivial word count is 1
            print("%s%s%d" % (words[i], "\t", 1))  # individual unigram count
            print("%s%s%d" % ("unigram_count", "\t", 1))  # total unigram count
            if i < words_in_line - 1:  # bigrams in line = ungrams in line - 1
                # individual bigram count
                print("%s%s%d" % (words[i] + " " + words[i + 1], "\t", 1))
                print("%s%s%d" % ("bigram_count", "\t", 1))  # total bigram count
            if i < words_in_line - 2:  # trigrams in line = unigrams - 2
                # individual trigram count
                print("%s%s%d" % (words[i] + " " + words[i + 1] + " " + words[i + 2], "\t", 1))
                print("%s%s%d" % ("trigram_count", "\t", 1))  # total trigram count


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
