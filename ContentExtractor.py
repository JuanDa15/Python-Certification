import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.coursera.org/learn/python-network-data/lecture/EaR2d/13-2-extensible-markup-language-xml'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,'html.parser')

Filename = 'testJD.txt'
Document = open(Filename,"a+")
tasg = soup('p')
counter = 40
n = 0
for tag in tasg:
    for line in tag.contents:     
        x = len(line) 
        for caracter in line:
            try:
                Document.write(caracter)
            except:
                continue
            if n == counter:
                Document.write('\n')
                n = 0
            n = n + 1




