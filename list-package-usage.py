#!/usr/bin/env python3
from json import load
from subprocess import run,PIPE
import urllib.request
import re

url = 'http://popcorn.voidlinux.org/'
list = urllib.request.urlopen(url).read().decode('utf-8')
regex = re.compile('[\d]{4}-[\d]{2}-[\d]{2}')
data = regex.findall(list)

url_json = 'http://popcorn.voidlinux.org/popcorn_' + data[-1] + '.json'
json = load(urllib.request.urlopen(url_json))

mypkgs = run(["xmypkgs"],stdout=PIPE).stdout.decode('utf-8')

for i in mypkgs.splitlines():
    print(i,end=' ')
    try:
        print(json["Packages"][i])
    except KeyError:
        print(0)
        pass

