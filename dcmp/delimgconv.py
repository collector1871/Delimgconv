'''
Created on 4 sty 2016
@author: collector1871
'''

import sys
import urllib
from bs4 import BeautifulSoup
from io import StringIO
import requests
from random import randint

def BierzUrl(var1):
    page = urllib.request.urlopen(var1)
    zupa1 = page.read()
    zupa = BeautifulSoup(zupa1, "html.parser")
    tags = zupa.findAll('img', style="width:99%;")
    koniec = str("\n".join(set(tag['src'] for tag in tags)))

    # wyswietlenie po 1 linii output - mozna pracowac z (line)

    koniec1 = StringIO(koniec)
    for line in koniec1:
        line2 = line.replace("?", "")
        line3 = line2.replace("\\", "")
        line4 = line3.replace("_", "")
        line5 = line4.replace(".", "")
        line6 = line5.replace("/", "")
        los1 = str(randint(0,9))
        los2 = str(randint(0,9))
        line7 = los1 + los2 + line6[-5] + line6[-6] + line6[-7]+ line6[-8]+ line6[-9]+ line6[-10]+".jpg"
        print(line7)
        urllib.request.urlretrieve(line, line7)

if __name__ == "__main__":
    BierzUrl(sys.argv[1])