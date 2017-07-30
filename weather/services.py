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
    future_time_ms = oldtime.time()*1000+float(time)
    day = datetime.fromtimestamp(future_time_ms/1000).day - datetime.now().day

    wthr_forecast = client.getForecastWeather(q=str(lat)+","+str(lon), days=(1+day))

    day_forecast = wthr_forecast['forecast']['forecastday'][(day)]
    retVal= checkAlert(day_forecast, future_time_ms)
    # retStr = str(retVal)
    return retVal


def checkAlert(forecast, future_time_ms):
    precip_in = forecast['hour'][datetime.fromtimestamp(future_time_ms/1000).hour]['precip_in']
    # logger.info(">>>>precipitation in inches is: %s", str(precip_in))
    # return precip_in
    if float(precip_in) > 0.0:
        return True
    else:
        return False

def getAllAlertsOnRoute(data):
    retArray = []
    for loc in data:
        location = json.dumps(loc)
        lat = float(json.loads(location)['latitude'])
        lon = float(json.loads(location)['longitude'])
        time = float(json.loads(location)['travelTime'])
        print("{\nlat: ",lat)
        print("\nlon: ",lon)
        print("\ntime:", time)
        print("\n}")
        if(getAlertByLatLong(lat,lon,time) is True):
            retArray.append({'latitude': lat, 'longitude': lon, 'alert': 'Raining here. Roads might be wet. Drive Carefully.'})

    return retArray