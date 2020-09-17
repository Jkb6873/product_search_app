from . import api
from flask import jsonify

@api.route('/search', methods=['GET'])
def search():
    return jsonify({}), 200
