# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:41:34 2020

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

#PART 3.1: It is the API endpoint that has a static subset of the Google Data...
#...This URL was provided by Coursera
#This API uses the same parameter (address) as the Google API. 
#This API also has no rate limit so you can test as often as you like. 
api_key = False
# If you have a Google Places API key, enter it here

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

#PART 3.2: Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#PART 3.3: Introduce de address (i.e. It is just an simple address)
# In the PART 3.3 we will encode this address (from "Unicode-String" to...
#...UTF8-Bytes)
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

#PART 3.4:In this phase we bring together the "Address" and the "API"
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

#PART 4: Create the socket and connect to the app...
#... through API (the URL thaT I will introduce is of the app from...
#...when I will get the informatino I want).
#In other words I am contacting a web service
    uh = urllib.request.urlopen(url, context=ctx)
    
#PART 5: Decoding the JSON
#We will decode this address (from UTF8-Bytes to "Unicode-String")
#Also we "read" the inforamtion
    data = uh.read().decode()
    
#PART 6: Parsing the JSON after the "loading"
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    lat = js['results'][0]['place_id']
    print(lat)
 
