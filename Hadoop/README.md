# N-Grams

## Results
for the file [cat.txt](cat.txt), the first map reduce job:
```bash
cat cat.txt | python map1.py |sort |python red1.py >> cat1.txt
```
The output of this job is [cat1.txt](cat1.txt). Bigrams = 24, unigrams = 21. trigrams = 18. Second Mar
```bash
cat cat1.txt | python map2.py 24 21 18 |sort |python red2.py >> cat2.txt
```
The probabilities are given in [cat2.txt](cat2.txt). 

## Running the jobs
The code failed on all of the homework files but I was able to run it on smaller files. The file 'juan.txt' in this folder was used to generate the results. Source: https://en.wikipedia.org/wiki/Juan_Rodríguez_Cabrillo
### Bash
Run the first map reduce
```bash
cat juan.txt | python map1.py |sort |python red1.py >> out1.txt
```
read the out.txt file for unigram_count, bigram_count and trigram_count values. The counts are unigram_count = 1492, bigram_count = 1475 and trigram_count = 1458

Then run the second map reduce job:
```bash
cat out1.txt |python map2.py 1492 1475 1458 |sort |python red2.py >> out2.txt
```
### Hadoop
Transfer the files to the Hadoop cluster home directory:
```cmd
hadoop fs -put map1.py
hadoop fs -put red1.py
hadoop fs -put map2.py
hadoop fs -put red2.py
hadoop fs -put hw1.2/*
hadoop fs -put juan.txt
```
To run the first map reduce job use:
```cmd
mapred streaming -file map1.py -mapper "python map1.py" -file red1.py -reducer "python red1.py" -input juan.txt -output out1
```
where hw1.2/ is the directory containing the text files, juan.txt is the text file used to test the code and out1 is the first output directory.

Then read out1 for unigram_count, bigram_count and trigram_count values:
```cmd
hadoop fs -cat out1/*
```
The counts are unigram_count = 1492, bigram_count = 1475 and trigram_count = 1458

Then run the second map reduce job:
```cmd
mapred streaming -file map2.py -mapper "python map2.py 1492 1475 1458" -file red2.py -reducer "python red2.py" -input out1/* -output out2
```
```cmd
haoop fs -cat out2/*
```

## Issues and Considerations

To make this assignment straightforward, a number of considerations were made that make the calculated n-gram count and conditional probabilities inaccurate.

### Characters considered

For the purpose of this assignment, all characters not in this set: [a-z, A-Z, 0-9] were replaced with spaces using the following regex:
```python
re.sub("[^a-zA-z0-9]", " ", text.lower())
```
#### Hypenated and Apostrophe Words:
The regex used would mistreat characters with hyphens or apostrophes such as `Don't` or `Mother-in-law` into `don t` and `mother in law`. 
#### Periods:
The regex used would also mistreat lines with periods in them. for instance, in the line `... this is something I hate. Puppie are adorable and ..." it will consider "i hate puppies" as a trigram (😢).
#### Partial Solution:
A more appropriate regex to include hyphenated and appsotrophe words might be given by the two options below. (source: https://stackoverflow.com/questions/27715581/):
```python
re.findall(r"(?!'.*')\b[\w'-]+\b", line.lower())
```
or
```python
re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", line.lower())
```
However, this would also include possessive words such as `professor's` which might be undesired. Also, this returns a list of words instead of a sigle string and Professor Juan warned us about using lists. 

### Line by line
#TODO Explain why bigram and trigram counts are not accurate since the mapper reads the input line by line

### Minimum line length
#TODO Explain why some bigrams and unigrams will be missed as we ignore lines with less than 3 words
