import sys
import string

def buildCoder(shift):
  coder = {}
  for i in range(26):
      coder[string.ascii_lowercase[i]] = string.ascii_lowercase[(shift + i) - 26]
  return coder

cipher_key = buildCoder(2)

chars = list(sys.stdin.read())

message = ''

for i in chars:
  if cipher_key.get(i):
    message += cipher_key[i]
  else:
    message += i

print message
