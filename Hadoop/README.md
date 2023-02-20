# N-Grams

## Considerations

### Characters considered

For the purpose of this assignment, all characters not in this set: [a-z, A-Z, 0-9] were replaced with spaces using the following regex:
```python
re.sub("[^0-9a-z]", " ", text.lower())
```
However this would ignore characters with hyphens or apostrophes such as `don't` or `mother-in-law`. A more appropriate regex to include these words can be given by the two options below. (source: https://stackoverflow.com/questions/27715581/):
```python
re.findall(r"(?!'.*')\b[\w'-]+\b", line.lower())
```
or
```python
re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*", line.lower())
```
However, this would also include possessive words such as `mother-in-law's`. Also, this returns a list of words instead of a sigle string and Professor Juan warned us about using lists. I am not sure if this is what he meant but it's already 3 pm and Sunday so I can't ask him.