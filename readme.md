### Delcampe images downloader and converter
dsfsdfds
* technologia: Python3
* kod źródłowy:   
https://github.com/collector1871/Delimgconv   

Celem programu jest pobranie wszystkich plików *.jpg z 500 aukcji (lista przedmiotów) ze strony delcampe.net.
Jako argument należy podać stronę użytkownika (sprzedawcy) z wyświetlonymi dokładnie 500 aukcjami.

#### Zależności

- python3
- python3: BeautifulSoup4, requests, urllib.request, random 

#### Użycie

Należy zainstalować niezbędne zależności, a następnie:

	python delimgconv.py <argument>

argument - strona użytkownika z 500 aukcjami na portalu delcampe.net

Przykłady argumentu:


      http://www.delcampe.net/items?reWriteUrl=Y&cat=-2&id_member=383357&language=E&searchString=&page=1&useAsDefault=N&layoutForm[listitemsperpage]=500

lub:  

      http://www.delcampe.net/items?reWriteUrl=Y&cat=-2&id_member=00531538&language=E&searchString=&page=1&useAsDefault=N&layoutForm[listitemsperpage]=500

#### Wynik
	
Pobrane pliki zostaną zapisane w formacie *.jpg (czas zależny jest od ilości zdjęć).

#### Screenshoty - przykład

![Start](https://raw.githubusercontent.com/collector1871/Delimgconv/master/Delimgconv1.jpg)

![pobrane fotki](https://raw.githubusercontent.com/collector1871/Delimgconv/master/Delimgconv2.jpg)
