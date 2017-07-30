from flask import Flask, request
from flask_restplus import Resource, fields, Namespace
import json

from weather import services

app = Flask(__name__)
ns = Namespace('APIXU Weather Service', description='APIXU Weather Service')


lat_lon_time_model = ns.model('lat_lon', {
    "lat": fields.String(required=True),
    "lon": fields.String(required=True),
    "time": fields.String(required=False)

})


@ns.route('/getWeatherByLatLong')
class getWeatherByLatLong(Resource):
    @ns.expect(lat_lon_time_model, validate=True)
    def post(self):
        """
            get weather based on latitude and longitude

            Example:
            ```   lat= 30.2672, lon= -97.7431 ```
        """
        data = json.dumps(request.get_json())
        lat = json.loads(data)['lat']
        lon = json.loads(data)['lon']
        time = json.loads(data)['time']
        response = services.getWeatherByLatLong(lat, lon, time)
        return response

@ns.route('/getAlertByLatLong')
class GetAlertByLatLong(Resource):
    @ns.expect(lat_lon_time_model, validate=True)
    def post(self):
        """
            get weather based on latitude and longitude

            Example:
            ```   lat= 30.2672, lon= -97.7431 ```
        """
        data = json.dumps(request.get_json())
        lat = json.loads(data)['lat']
        lon = json.loads(data)['lon']
        time = json.loads(data)['time']
        response = services.getAlertByLatLong(lat, lon, time)
        return response
