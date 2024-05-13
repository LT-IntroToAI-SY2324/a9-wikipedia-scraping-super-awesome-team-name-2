import re

# . (dot) any char
# \w word char
# \d digit
# \s whitespace \S non-whitespace
# + 1 or more
# * 0 or more
# [] set of char
# {} a number of instances

string = "called piiig"
pat = re.compile("iig")
result = pat.search(string)
print(result)
print(result.group())

string = "called piiig"
pat = re.compile("xiig")
result = pat.search(string)
print(result)

pat.recompile("called")
result = pat.match(string)
print(result)

pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("x...g")
result = pat.search(string)
# print(result.group())