import re
import sys

#regex = re.compile('[A-Z]{3}[a-z][A-Z]{3}')
regex = re.compile('(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])')
matches = []

for line in sys.stdin:
  matches += regex.findall(line)

string = ''
for i in matches:
  string += i[3]

print string
