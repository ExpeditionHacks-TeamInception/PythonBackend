import requests
import json

url = "https://geocoder.cit.api.here.com/6.2/geocode.json?"
app_id = "8zbmKsTdRGcXP9qI8pI5"
app_code = "wgchKRAQBczyCzYKVW1YdQ"
def getLatLang(houseNumber, street, city):
    payload = {'housenumber': houseNumber, 
               'street': street,
               'city': city,
               'app_id': app_id, 
               'app_code': app_code, 
               'gen': '8'}
    response = requests.get(url, params=payload)
    print response.url
    return json.loads(response.text)

def getLatLangs(address):
    
    #mydict = { 'searchtext' : address, 'app_id' : "8zbmKsTdRGcXP9qI8pI5", 'app_code' : "wgchKRAQBczyCzYKVW1YdQ", 'gen' : "8"}
    #encryptedUrl = urllib.urlencode(mydict, 'utf-8')
    #print encryptedUrl
    
    #urlExt = "searchtext=200%20S%20Mathilda%20Sunnyvale%20CA&app_id=&app_code=wgchKRAQBczyCzYKVW1YdQ&gen=8"

    #url1 = "https://geocoder.cit.api.here.com/6.2/geocode.json?app_id=8zbmKsTdRGcXP9qI8pI5&app_code=wgchKRAQBczyCzYKVW1YdQ&gen=9&"+urllib.urlencode(searchtext)
    #payload = {'searchtext': address, 'app_id': "8zbmKsTdRGcXP9qI8pI5", 'app_code':"wgchKRAQBczyCzYKVW1YdQ", 'gen': "8"}
    #ret = requests.get(urllib.quote(url+'?'+'searchtext='+address+'&'+'app_id=8zbmKsTdRGcXP9qI8pI5'+'&'+'app_code=wgchKRAQBczyCzYKVW1YdQ'+'&'+'gen=8'))
    #ret = requests.get(url, payload)
    #print urllib.urlencode(url)
    #ret = requests.get(url)
    #print ret
    
    payload = {'searchtext': address, 'app_id': app_id, 'app_code': app_code, 'gen': '8'}
    
    r = requests.get(url, params=payload)
    #print r.url
    return json.loads(r.text)