#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys


def read_input(input):
    for line in input:
        # split the line into words; keep returning each word - for each line in the input, return each line
        yield line.split()


def main(unigrams, bigrams, trigrams, separator="\t"):
    # default separator is a tab - which is \t - can change it to something else
    # input comes from STDIN (standard input) - read and input from standard input
    ngram = read_input(sys.stdin)
    total_ngrams = [unigrams, bigrams, trigrams]
    for words in ngram:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        n = len(words) - 1  # n-grams length
        prob_ngram = int(words[n]) / total_ngrams[n - 1]  # prob of ngram
        key = value = words[0]
        for i in range(1, n):
            value = key + " " + words[i]
            if i < n - 1:
                key = key + " " + words[i]
        if n != 3:
            print("%s%s%s" % (value, separator, str(prob_ngram)))
        if n > 1:
            print("%s%s%s" % (key, separator, value + " " + str(prob_ngram)))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main(unigrams=int(sys.argv[1]), bigrams=int(sys.argv[2]), trigrams=int(sys.argv[3]))
