'''
Created on 4 sty 2016

@author:
'''

import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('http://www.delcampe.net/page/item/id,321490576,var,indigenas-mossumbes-editon-raul-peres-leiro-novo-redondo--mauvais-etat-timbre-decoupe--recto-verso-,language,E.html').read()
zupa = BeautifulSoup(page)
tags = zupa.findAll('img')

print(tags)