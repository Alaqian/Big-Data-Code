# N-Grams

## Running the jobs
First transfer all the code to Hadoop home directory:
```cmd
hadoop fs -put map1.py
hadoop fs -put red1.py
hadoop fs -put map2.py
hadoop fs -put red2.py
hadoop fs -put hw1.2/*
```
To run the first map reduce job use:
```cmd
mapred streaming -file map1.py -mapper "python map1.py" -file red1.py -reducer "python red1.py" -input hw1.2/* -output out1
```
where hw1.2/ is the directory containing the text files and out1 is ythe first output directory

Then read out1 using for unigram_count, bigram_count and trigram_count values:
```cmd
hadoop fs -cat out1/*
```
lets say unigram_count = 1000, bigram_count =999 and trigram_count = 998

Then run the second map reduce job:
```cmd
mapred streaming -file map2.py -mapper "python map2.py 1000 999 9998" -file red2.py -reducer "python red2.py" -input out1/* -output out2

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
