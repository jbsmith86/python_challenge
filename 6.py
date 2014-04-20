import os
import re
import zipfile

os.chdir('channel')
regnum = re.compile(r'^\d{1,}$')

current = '90052'

while regnum.match(current):
  filename = current + '.txt'
  txt_file = open(filename, 'r').read()
  current = txt_file.split(' ')[-1]
  if regnum.match(current):
    print current
  else:
    print txt_file

hint = ''
os.chdir('..')
z = zipfile.ZipFile('channel.zip')
current = '90052'

os.chdir('channel')
while regnum.match(current):
  filename = current + '.txt'
  hint += z.getinfo(filename).comment
  txt_file = open(filename, 'r').read()
  current = txt_file.split(' ')[-1]

print hint
