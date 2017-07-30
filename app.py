from flask import Flask
from flask_restplus import Api
from hereapis.endpoints.hereendpoints import ns as ns_hereapi
from weather.endpoints import ns as ns_apixu


app = Flask(__name__)
api = Api(app, version='1.0', title='Here maps API',
    description='Here Service API'
)

api.add_namespace(ns_hereapi, path='/here')
api.add_namespace(ns_apixu, path='/weather/v1')


if __name__ == '__main__':
    app.run(debug=True,port=5056,host='0.0.0.0')
