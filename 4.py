#!/usr/bin/env python3
import urllib.request
print(urllib)
template = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'
url = urllib.request.urlopen(template.format(12345))
string = url.read().decode('utf-8')
next_int = string.split(' ')[-1]
while True:
    print(next_int)
    url = urllib.request.urlopen(template.format(next_int))
    string = url.read().decode('utf-8')
    next_int = string.split(' ')[-1]
