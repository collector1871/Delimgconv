'''
Created on 4 sty 2016
@author: collector1871
'''
import sys
import urllib.request
from bs4 import BeautifulSoup
from io import StringIO


try:
    var1 = sys.argv[1]
except IndexError:
    var = "pusta"

page = urllib.request.urlopen(var1)

zupa1 = page.read()

zupa = BeautifulSoup(zupa1, "html.parser")
tags = zupa.findAll('img', style="width:99%;")
koniec = str("\n".join(set(tag['src'] for tag in tags)))

# wyswietlenie po 1 linii output - mozna pracowac z (lin)e
koniec1 = StringIO(koniec)
for line in koniec1:
    print(line)