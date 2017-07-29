from flask import Flask, request
from flask_restplus import Resource, fields, Namespace
import json

from hereapis import hereService

ns = Namespace('hereapis', description='Operations related to here api')
app = Flask(__name__)


app = Flask(__name__)
ns = Namespace('Here maps Service', description='Here maps Service API Version 1.0')


address_model = ns.model('address', {
    "street": fields.String(required=True),
    "city": fields.String(required=True),
    "zipcode":fields.List(fields.String,required=True)

})


@ns.route('/v1/latlang')
class LatLong(Resource):
    @ns.expect(address_model, validate = True)
    def post(self):
        """
            get lat long based on address
        """
        data = json.dumps(request.get_json())
        street = json.loads(data)['street']
        response = hereService.getLatLang(data)
        return json.loads(response)
