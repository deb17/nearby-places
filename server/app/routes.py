from app import app
from flask import request, jsonify

from app.nearby import nearby

@app.route('/')
def index():

    lat = float(request.args.get('lat') or 0)
    lon = float(request.args.get('lon') or 0)
    string = request.args.get('s')
    addr = request.args.get('addr')

    data = nearby(string, addr, lat, lon)

    return jsonify(data)

