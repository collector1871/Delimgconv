'''
Created on 4 sty 2016

'''
import sys
import urllib.request
import wget
from bs4 import BeautifulSoup
from io import StringIO
from delimgconv import BierzUrl


def BierzUrl2(var1):
    page = urllib.request.urlopen(var1)
    zupa1 = page.read()
    zupa = BeautifulSoup(zupa1, "html.parser")
    tags = zupa.findAll('div', style="padding:5px;text-align:center;")
    szukanieDivu = zupa.findAll('div', style="padding:5px;text-align:center;")
    for div in szukanieDivu:
        koniec3 = str((div.a['href']))
        koniec4 = str("http://www.delcampe.net/" + koniec3)
        print(koniec4)
        BierzUrl(koniec4)



if __name__ == "__main__":
    BierzUrl2(sys.argv[1])