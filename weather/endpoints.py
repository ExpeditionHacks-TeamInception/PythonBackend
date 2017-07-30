from flask import Flask, request
from flask_restplus import Resource, fields, Namespace
import json
import requests
from hereapis import hereService

from weather import services

app = Flask(__name__)
ns = Namespace('APIXU Weather Service', description='APIXU Weather Service')


lat_lon_time_model = ns.model('lat_lon', {
    "lat": fields.String(required=True),
    "lon": fields.String(required=True),
    "time": fields.String(required=True)

})

lat_lon_model = ns.model('lat_lon', {
    "lat": fields.String(required=True),
    "lon": fields.String(required=True)
})


way_points_model = ns.model('way_points_model', {
    "waypoint0": fields.String(required=True),
    "waypoint1": fields.String(required=True),

})


@ns.route('/getWeatherByLatLong')
class getWeatherByLatLong(Resource):
    @ns.expect(lat_lon_time_model, validate=True)
    def post(self):
        """
            get weather based on latitude and longitude

            Example:
            ```   lat= 30.2672, lon= -97.7431, time=0 (seconds from now) ```
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
            ```   lat: 30.2672, lon= -97.7431, time= 0.0```
        """
        data = json.dumps(request.get_json())
        lat = json.loads(data)['lat']
        lon = json.loads(data)['lon']
        time = json.loads(data)['time']
        response = services.getAlertByLatLong(lat, lon, time)
        return response

@ns.route('/getAllAlertsOnRoute')
class GetAllAlertsOnRoute(Resource):
    def post(self):
        """
        Get All Lat-Longs on the route for which there is a weather alert
            Example:
            ```
            {
                "waypoint0": "52.5160,13.3779",
                "waypoint1": "52.5206,13.3862"
            }
            ```
        """
        data = json.dumps(request.get_json())
        # start = json.loads(data)['waypoint0']
        # dest = json.loads(data)['waypoint1']
        resp1 = hereService.getWayPonintsbtwLocations(route=data)

        response = services.getAllAlertsOnRoute(resp1)
        return response
