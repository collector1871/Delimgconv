'''
Created on 4 sty 2016

@author: collector1871
'''
import sys
import urllib.request
from bs4 import BeautifulSoup

try:
    var1 = sys.argv[1]
except IndexError:
    var = "pusta"

page = urllib.request.urlopen(var1)

zupa1 = page.read()

zupa = BeautifulSoup(zupa1, "html.parser")
tags = zupa.findAll('img', style="width:99%;")
koniec = str("\n".join(set(tag['src'] for tag in tags)))

print(koniec)