import requests
import json

address_url = "https://geocoder.cit.api.here.com/6.2/geocode.json?"
route_url = "https://route.cit.api.here.com/routing/7.2/calculateroute.json?"
reversecode_url = "https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json?"
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
weather_forecast = "http://api.openweathermap.org/data/2.5/forecast?"

app_id = "8zbmKsTdRGcXP9qI8pI5"
app_code = "wgchKRAQBczyCzYKVW1YdQ"

def getLatLang(houseNumber, street, city):
    payload = {'housenumber': houseNumber, 
               'street': street,
               'city': city,
               'app_id': app_id, 
               'app_code': app_code, 
               'gen': '8'}
    response = requests.get(address_url, params=payload)
    #print response.url
    latLongData = parseJsonData(json.loads(response.text))
    return latLongData

def getLatLongs(address):
    
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
    
    r = requests.get(address_url, params=payload)
    #print r.url
    return json.loads(r.text)

def getCityByLatLong(prox):
    payload = {'prox': prox, 'app_id': app_id, 'app_code': app_code, 'gen': '9', 'mode': 'retrieveAddresses'}
    r = requests.get(reversecode_url, params=payload)
    return json.loads(r.text)

def getWeatherByZipcode(zipcode):
    payload = {'zip': zipcode, 'APPID': "5b2b1fdcd2fc36317168cb007e59f754"}
    r = requests.get(weather_url, payload)
    print r.url
    return json.loads(r.text)

def getWeatherByCity(cityname):
    city_payload = {'q': cityname, 'APPID': "5b2b1fdcd2fc36317168cb007e59f754"}
    r = requests.get(weather_forecast, city_payload)
    print r.url
    return json.loads(r.text)

def getWeatherByLatLong(lat, lon):
    payload = {'lat': lat,'lon': lon, 'APPID': "5b2b1fdcd2fc36317168cb007e59f754"}
    r = requests.get(weather_forecast, payload)
    print r.url
    return json.loads(r.text)

def parseJsonData(data):
    parsedData = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]
    print parsedData
    return parsedData
