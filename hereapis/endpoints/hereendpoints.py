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

@ns.route('/v1/latlang')
class LatLong(Resource):
    @ns.expect(address_model, validate = True)
    def post(self):
        """
            get lat long based on address
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
        """
        response = hereService.getLatLangs(address)
        return response
