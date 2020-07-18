import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_699250.xml'
if len(address) < 1: quit()

tree = ET.fromstring(urllib.request.urlopen(address).read())
listcomment = tree.findall('comments/comment/count')
result = 0
for i in listcomment:
    result = result + int(i.text)


print(result)