# N-Grams

**Note**: This homework was completed using the cloudera docker image: https://hub.docker.com/r/cloudera/quickstart/

#TODO Add instructions on downloading, installing and running the docker image

## Issues and Considerations

To make this assignment straightforward, a number of considerations were made that make the calculated n-gram count and conditional probabilities inaccurate.

### Characters considered

For the purpose of this assignment, all characters not in this set: [a-z, A-Z, 0-9] were replaced with spaces using the following regex:
```python
re.sub("[^a-zA-z0-9]", " ", text.lower())
```
#### Hypenated and Apostrophe Words
The regex used would mistreat characters with hyphens or apostrophes such as `Don't` or `Mother-in-law` into `don t` and `mother in law`. 
#### Periods
The regex used would also mistreat lines with periods in them. for instance, in the line `... this is something I hate. Puppie are adorable and ..." it will consider "i hate puppies" as a trigram (😢).
#### Potential Solution for Hypenated and Apostrophe Words
A more appropriate regex to include hyphenated and appsotrophe words might be given by the two options below. (source: https://stackoverflow.com/questions/27715581/):
```python
re.findall(r"(?!'.*')\b[\w'-]+\b", line.lower())
```
or
```python
re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", line.lower())
```
However, this would also include possessive words such as `professor's` which might be undesired. Also, this returns a list of words instead of a sigle string and Professor Juan warned us about using lists. I am not sure if this is what he meant but it's already 3 pm and Sunday so I can't ask him.