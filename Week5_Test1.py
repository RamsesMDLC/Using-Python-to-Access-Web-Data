# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:45:46 2020

@author: USUARIO
"""
#PART 1.1: IMPORTING LIBRARIES AND OTHERS INSTRUMENTS

#I wil use "urllib" because I need to "to do the socket" and "get info (txt o HTML)"
import urllib.request, urllib.parse, urllib.error
#I wil use "ElemenyTree" because I need to parse XML text.
import xml.etree.ElementTree as ET
#I wil use "import ssl" because of "ctx code"
import ssl

#PART 1.2: STUFF THAT I DO NOT USE
#I do not use "import re" because this homework it is not relate...
#...with "regular expressions"
# I do not use "Beautiful Soup" because I am nto interested...
#... in transforming (UTF-8 to Unicode). Also I am not...
#...interested in a HTML superparser.

#PART 2: Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#PART 3: Create the socket and read de webpage (the URL tha I will introduce)
URL = input('Enter - ')
XMLFile = urllib.request.urlopen(URL, context=ctx).read()

#PART 4: Parsing the XML
XMLTree = ET.fromstring(XMLFile)
#This "findall" is in a tree
FindComment = XMLTree.findall("comments/comment")
FinalSum = 0
#This "for" is in a tree
for Item in FindComment:
    CountNumberString = (Item.find("count").text)
    CountNumberInt = int(CountNumberString)
    FinalSum = CountNumberInt + FinalSum
    #Because the "CountNumber" variable is a string, I will convert...
    #...the "string" in "int" and then "sum up".
print (FinalSum)