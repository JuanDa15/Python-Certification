#fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.html')

...
# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
   # Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#html = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
"""
import urllib.request
from bs4 import BeautifulSoup


url = input('Enter a valid url: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

result = 0

tags = soup('span')
for tag in tags:
    result = int(tag.contents[0]) + result

print (result)
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n=1

url = input('Enter URL: ')
count= int(input('Enter count: '))+1
pos=int(input('Enter position: '))
new = url
while n<count:
    if new == url:
        html = urllib.request.urlopen(url).read()
        print('Retrieving', url)
    html = urllib.request.urlopen(new).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    my_tags=tags[pos-1]
    new=my_tags.get('href', None)
    print('Retrieving' , new)
    n=n+1

print(my_tags.contents[0])