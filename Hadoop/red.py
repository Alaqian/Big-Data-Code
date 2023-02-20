import sys

prev_word = None
prev_count = 0

for line in sys.stdin:
    word, count = line.strip().split("\t")
    count = int(count)

    if prev_word == word:
        prev_count += count
    else:
        if prev_word:
            print("%s%s%d" % (prev_word, "\t", count))
        prev_count = count
        prev_word = word

if prev_word == word:
    print("%s%s%d" % (prev_word, "\t", count))
