# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:09:03 2019

@author: USUARIO
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the numbers
tags = soup('span')
TotalSum = 0
for tag in tags:
    Numberx = int(tag.contents[0])
    TotalSum = TotalSum + Numberx
print(TotalSum)

