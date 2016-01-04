'''
Created on 4 sty 2016

@author:
'''

import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://www.delcampe.net/page/item/id,321490576,var,indigenas-mossumbes-editon-raul-peres-leiro-novo-redondo--mauvais-etat-timbre-decoupe--recto-verso-,language,E.html')

zupa1 = page.read()

zupa = BeautifulSoup(zupa1, "html.parser")
tags = zupa.findAll('img', style="width:99%;")

# print "\n".join(tags)

for word in tags:
    print(word)
# print(tags)