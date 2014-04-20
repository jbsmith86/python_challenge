import sys

hist = {}
string = ''

for line in sys.stdin:
  linearray = list(line)
  for i in linearray:
    if i in 'aeilquty':
      string += i
    if hist.get(i):
      hist[i] += 1
    else:
      hist[i] = 1

print hist
print string
