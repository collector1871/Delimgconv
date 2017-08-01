### Delcampe images downloader and converter
dfgdf
* technologia: Python3
* kod ��r��d��owy:   
https://github.com/collector1871/Delimgconv   

Celem programu jest pobranie wszystkich plik��w *.jpg z 500 aukcji (lista przedmiot��w) ze strony delcampe.net.
Jako argument nale��y poda�� stron�� u��ytkownika (sprzedawcy) z wy��wietlonymi dok��adnie 500 aukcjami.

#### Zale��no��ci

- python3
- python3: BeautifulSoup4, requests, urllib.request, random 

#### U��ycie

Nale��y zainstalowa�� niezb��dne zale��no��ci, a nast��pnie:

	python delimgconv.py <argument>

argument - strona u��ytkownika z 500 aukcjami na portalu delcampe.net

Przyk��ady argumentu:


      http://www.delcampe.net/items?reWriteUrl=Y&cat=-2&id_member=383357&language=E&searchString=&page=1&useAsDefault=N&layoutForm[listitemsperpage]=500

lub:  

      http://www.delcampe.net/items?reWriteUrl=Y&cat=-2&id_member=00531538&language=E&searchString=&page=1&useAsDefault=N&layoutForm[listitemsperpage]=500

#### Wynik
	
Pobrane pliki zostan�� zapisane w formacie *.jpg (czas zale��ny jest od ilo��ci zdj����).

#### Screenshoty - przyk��ad

![Start](https://raw.githubusercontent.com/collector1871/Delimgconv/master/Delimgconv1.jpg)

![pobrane fotki](https://raw.githubusercontent.com/collector1871/Delimgconv/master/Delimgconv2.jpg)
