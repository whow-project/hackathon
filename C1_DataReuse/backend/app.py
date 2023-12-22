from flask import Flask
from flask_cors import CORS

from api.bathw import bathw_api
from api.datasets import datasets_api
from api.landcs import landcs_api
from api.regioni import regioni_api

app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False
app.register_blueprint(datasets_api, url_prefix="/api/datasets")
app.register_blueprint(bathw_api, url_prefix="/api/bathw")
app.register_blueprint(landcs_api, url_prefix="/api/landcs")
app.register_blueprint(regioni_api, url_prefix="/api/regioni")
