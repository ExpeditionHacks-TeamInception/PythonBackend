import requests
import json
from hereapis.calc import getDistance

address_url = "https://geocoder.cit.api.here.com/6.2/geocode.json?"
route_url = "https://route.cit.api.here.com/routing/7.2/calculateroute.json?"
reversecode_url = "https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json?"
weather_url = "http://api.openweathermap.org/data/2.5/weather?"
weather_forecast = "http://api.openweathermap.org/data/2.5/forecast?"
way_points = "https://route.cit.api.here.com/routing/7.2/calculateroute.json?"

app_id = "8zbmKsTdRGcXP9qI8pI5"
app_code = "wgchKRAQBczyCzYKVW1YdQ"

#APPID for OpenWeatherMap API's
APPID = "5b2b1fdcd2fc36317168cb007e59f754"

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
    latLongData = parseJsonData(json.loads(r.text))
    return latLongData
    #return json.loads(r.text)

def getCityByLatLong(prox):
    payload = {'prox': prox, 'app_id': app_id, 'app_code': app_code, 'gen': '9', 'mode': 'retrieveAddresses'}
    r = requests.get(reversecode_url, params=payload)
    return json.loads(r.text)

def getWeatherByZipcode(zipcode):
    payload = {'zip': zipcode, 'APPID': APPID}
    r = requests.get(weather_url, payload)
    print r.url
    return json.loads(r.text)

def getWeatherByCity(cityname):
    city_payload = {'q': cityname, 'APPID': APPID}
    r = requests.get(weather_forecast, city_payload)
    print r.url
    return json.loads(r.text)

def getWeatherByLatLong(lat, lon):
    payload = {'lat': lat,'lon': lon, 'APPID': APPID}
    r = requests.get(weather_forecast, payload)
    print r.url
    return json.loads(r.text)

def parseJsonData(data):
    parsedData = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]
    print parsedData
    return parsedData

def getWayPonintsbtwLocations(start, dest):
    payload = {'waypoint0': start,'waypoint1': dest, 'mode':"fastest;car;traffic:enabled", 'departure':"now",'app_id': app_id, 'app_code': app_code}
    r = requests.get(way_points, payload)
    print r.url
    wayPointsData = getWayPointsList(json.loads(r.text))
    #return json.loads(r.text)
    return wayPointsData
    
def getWayPointsList(data):
    pointsArray = []
    if len(data) > 0:
        wayPointsData = data['response']['route'][0]['leg'][0]['maneuver']
    
    if len(wayPointsData) > 0:
        for arrayItem in wayPointsData:
            pointsArray.append({"latlong" : arrayItem['position'], "travelTime" : arrayItem['travelTime']*1000})
        
   
        index = 0
        totalDistance = 0
        newWaypoints = []
        if len(pointsArray) > 0 :
            lat1 = pointsArray[0]['latlong']['latitude']
            long1 = pointsArray[0]['latlong']['longitude']
            newWaypoints.append({"latitude": lat1, "longitude": long1})
            index += 1
            templat = pointsArray[0]['latlong']['latitude']
            templong = pointsArray[0]['latlong']['longitude']                   
            while index < len(pointsArray)-1:
                #print(index, items[index])
                #lat1 = pointsArray[index]['latlong']['latitude']
                #long1 = pointsArray[index]['latlong']['longitude']
                lat2 = pointsArray[index+1]['latlong']['latitude']
                long2 = pointsArray[index+1]['latlong']['longitude']
                distance = getDistance(templat, templong, lat2, long2)
                print("diastance:", distance)
                totalDistance += distance
                if(distance > 50):
                    newWaypoints.append({"latitude": lat2, "longitude": long2})
                    templat = lat2
                    templong = long2
                    
                index += 1
            latLast = pointsArray[len(pointsArray)-1]['latlong']['latitude']
            longLast = pointsArray[len(pointsArray)-1]['latlong']['longitude']
            newWaypoints.append({"latitude": latLast, "longitude": longLast})
        print("new points array length:", len(newWaypoints))
        print("new points:", newWaypoints)
        print("total distance:", totalDistance)
        
    print("old points array length:", len(pointsArray))
    return newWaypoints

