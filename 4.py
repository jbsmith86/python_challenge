import urllib
import re

current = '12345'
regnum = re.compile(r'^\D{1,}$')

for i in range(400):
  data = urllib.urlencode({'nothing' : current})
  page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php' + '?' + data).read()
  current = page.split(' ')[-1]
  if regnum.match(current):
    print current
