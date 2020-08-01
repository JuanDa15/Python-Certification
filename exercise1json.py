import urllib.request,urllib.parse,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter Location: ')
    if len(addres) < 1: break