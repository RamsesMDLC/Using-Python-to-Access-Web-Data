# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 01:41:42 2020

@author: USUARIO
"""

#PART 1.1: IMPORTING LIBRARIES AND OTHERS INSTRUMENTS

#I wil use "urllib" because I need to "to do the socket" and "get info (txt o HTML)"
import urllib.request, urllib.parse, urllib.error
#I wil use "JSON" because I need to parse JSON text.
import json
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

#PART 3: Create the socket and connect to the app...
#... through the URL tha I will introduce
URL = input('Enter - ')
JSONFile = urllib.request.urlopen(URL, context=ctx).read()

#PART 4: Parsing the JSON
JSONFileLoad = json.loads(JSONFile)

#PART 5: Because I print the PART 4, I figured out that this information...
#...was a Dictionary-List-Dictionary. Therefore, I start to the code of...
#...a Dictionary
Value1 = JSONFileLoad["comments"]

#PART 6: Because I print the PART 4, I figured out that this information...
#...was a Dictionary-List-Dictionary. Therefore, I continute to the code of...
#...a List in the For, an internally in the For, with the code of a...
#...Dictionary
FinalSum = 0
for Items in Value1:
    Value2 = Items["count"]
    #Because the "Value2" variable is a string, I will convert...
    #...the "string" in "int" and then "sum up".
    Value2Int = int(Value2)
    FinalSum = Value2Int + FinalSum
print (FinalSum)
