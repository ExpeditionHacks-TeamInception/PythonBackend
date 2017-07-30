from flask import Flask, request
from flask_restplus import Resource, fields, Namespace
import json

from hereapis import hereService

app = Flask(__name__)
ns = Namespace('Here maps Service', description='Here maps Service API Version 1.0')


address_model = ns.model('address', {
    "HouseNumber": fields.Integer(required=True),
    "Street": fields.String(required=True),
    "city": fields.String(required=True)

})
lat_lon_model = ns.model('lat_lon', {
    "lat": fields.String(required=True),
    "lon": fields.String(required=True),

})

@ns.route('/v1/latlang')
class LatLong(Resource):
    @ns.expect(address_model, validate = True)
    def post(self):
        """
            get lat long based on address
            
            Example:
            ```
            {
              "city": "Austin",
              "Street": "Tapadera Trace Ln",
              "HouseNumber": 5700
            }
            ```
            
        """
        data = json.dumps(request.get_json())
        houseNumber = json.loads(data)['HouseNumber']
        street = json.loads(data)['Street']
        city = json.loads(data)['city']
        #address = '&housenumber='+houseNumber+'&street='+street+'&city='+city
        response = hereService.getLatLang(houseNumber, street, city)
        return response
    
@ns.route('/v1/latlang/<address>')
class LatLongs(Resource):
    def get(self, address):
        """
            get lat long based on address string
            
            Example: 
            ```  5700 Tapadera Trace Ln, Austin, TX  ```
        """
        response = hereService.getLatLongs(address)
        return response
    
@ns.route('/v1/latlang/<prox>')
class CityAddress(Resource):
    def get(self, prox):
        """
            get city based on Lat Long
            
            Example: 
            ```  50.112,8.683,100 ```
        """
        response = hereService.getCityByLatLong(prox)
        return response
    
@ns.route('/v1/weather/<zipcode>')
class getWeatherByZip(Resource):
    def get(self, zipcode):
        """
            get weather based on zipcode and country code
            
            Example: 
            ```  78727,us ```
        """
        response = hereService.getWeatherByZipcode(zipcode)
        return response

@ns.route('/v1/weather')
class getWeatherByLatLong(Resource):
    @ns.expect(lat_lon_model, validate = True)
    def post(self):
        """
            get weather based on lat lon
            
            Example: 
            ```   lat= 35, lon= 139 ```
        """
        data = json.dumps(request.get_json())
        lat = json.loads(data)['lat']
        lon = json.loads(data)['lon']
        response = hereService.getWeatherByLatLong(lat, lon)
        return response

@ns.route('/v1/weather/forecast/<cityname>')
class getWeatherByCityName(Resource):
    def get(self, cityname):
        """
            get weather based cityname
            
            Example: 
            ```  Austin,us ```
        """
        response = hereService.getWeatherByCity(cityname)
        return response
