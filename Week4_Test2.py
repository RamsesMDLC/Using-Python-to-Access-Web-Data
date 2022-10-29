# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 17:09:03 2019

@author: USUARIO
"""

#STAGE1

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL1 = tag.get('href', None)
        url = NewURL1
        print(NewURL1)

#STAGE2

url = NewURL1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL2 = tag.get('href', None)
        url = NewURL2
        print(NewURL2)
        
#STAGE3

url = NewURL2
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL3 = tag.get('href', None)
        url = NewURL3
        print(NewURL3)
        
#STAGE4

url = NewURL3
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL4 = tag.get('href', None)
        url = NewURL4
        print(NewURL4)
        
#STAGE5

url = NewURL4
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL5 = tag.get('href', None)
        url = NewURL5
        print(NewURL5)
        
#STAGE6

url = NewURL5
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL6 = tag.get('href', None)
        url = NewURL6
        print(NewURL6)
        
#STAGE7

url = NewURL6
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
X = 0
for tag in tags:
    X = X+1
    if X==18:
        NewURL7 = tag.get('href', None)
        url = NewURL7
        print(NewURL7)