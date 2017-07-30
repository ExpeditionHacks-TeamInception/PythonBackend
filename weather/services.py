import json
import logging
import time as oldtime

from datetime import datetime
from apixu.client import ApixuClient, ApixuException

api_key = 'a0b62bd3ffe2434c9c814358173007'
client = ApixuClient(api_key)


logger = logging.getLogger(__name__)

def getWeatherByLatLong(lat, lon, time):
    forecast = client.getForecastWeather(q=str(lat)+","+str(lon))
    return forecast


def getAlertByLatLong(lat, lon, time):
    future_time_ms = oldtime.time()+float(time)
    day = datetime.fromtimestamp(future_time_ms).day - datetime.now().day

    wthr_forecast = client.getForecastWeather(q=str(lat)+","+str(lon), days=(1+day))

    day_forecast = wthr_forecast['forecast']['forecastday'][(day)]
    retVal= checkAlert(day_forecast, future_time_ms)
    # retStr = str(retVal)
    return retVal


def checkAlert(forecast, future_time_ms):
    alertStr = ""
    precip_mm = forecast['hour'][datetime.fromtimestamp(future_time_ms).hour]['precip_mm']
    vis_km = forecast['hour'][datetime.fromtimestamp(future_time_ms).hour]['vis_km']
    temp_c = forecast['hour'][datetime.fromtimestamp(future_time_ms).hour]['temp_c']
    dewpoint_c = forecast['hour'][datetime.fromtimestamp(future_time_ms).hour]['dewpoint_c']
    wind_mph = forecast['hour'][datetime.fromtimestamp(future_time_ms).hour]['wind_mph']
    # logger.info(">>>>precipitation in inches is: %s", str(precip_in))
    # return precip_in
    if (float(precip_mm) > 0.0 and float(precip_mm) <= 0.5):
        alertStr+='Light Rainfall. Hydroplaning Alert!\n'
    if (float(precip_mm) > 0.5 and float(precip_mm) <= 4.0):
        alertStr+='Moderate Rainfall.\n'
    if (float(precip_mm) > 4.0 and float(precip_mm) <= 8.0):
        alertStr+='Heavy Rainfall. Low Visibility.\n'
    if (float(precip_mm) > 8.0):
        alertStr+='Torrential Rainfall. Find Shelter!\n'
    if float(vis_km) < 1.0:
        alertStr += 'Low Visibility. Drive Carefully!\n'
    if (float(temp_c) < 2.0 and float(precip_mm) > 0.0):
        alertStr += 'Road Icing Alert. Use Extreme Caution!\n'
    if float(temp_c) <= 0.0:
        alertStr += 'Freezing Conditions!\n'
    # if ((float(temp_c)-float(dewpoint_c)) < 1.0 or (float(dewpoint_c)-float(temp_c)) < 1.0):
        #alertStr += 'Fog Conditions. Low Visibility Alert!\n'
    if float(wind_mph) > 30.0:
        alertStr += 'Extreme Winds. Drive Carefully!\n'

    return alertStr


def getAllAlertsOnRoute(data):
    retArray = []
    count = 1
    for loc in data:
        location = json.dumps(loc)
        lat = float(json.loads(location)['latitude'])
        lon = float(json.loads(location)['longitude'])
        time = float(json.loads(location)['travelTime'])
        print(count)
        print("lat: ",lat)
        print("lon: ",lon)
        print("time:", time)
        print(" \n ")
        count+=1
        alertStr = getAlertByLatLong(lat, lon, time)
        if(len(alertStr) >0):
            retArray.append({'latitude': lat, 'longitude': lon, 'alert': alertStr})

    return retArray