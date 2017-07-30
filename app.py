from flask import Flask
from flask_restplus import Api
from hereapis.endpoints.hereendpoints import ns as ns_hereapi
from flask_cors import CORS



app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app, version='1.0', title='Here maps API',
    description='Here Service API'
)

api.add_namespace(ns_hereapi, path='/here')


if __name__ == '__main__':
    app.run(debug=True,port=5056,host='0.0.0.0')
