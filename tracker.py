import requests
from flask import Flask, request, jsonify

bitso_app = Flask(__name__)
bitso_api_url = "https://api.bitso.com/v3/"

@bitso_app.route("/show/<string:api_name>/")
def show(api_name, book=None, aggregate=True, marker=None, sort="desc", limit=25):
    return jsonify(get_public_bitso_api(api_name, request.args))

"""
    Simple API that performs a GET request on Bitso REST APIs

    Parameters
    ----------
    api_name : str
        a string that represents the API to request the GET method
    params : dict, optional
        parameters needed for the GET method (default is None)

    Returns
    -------
    list
        a list of dictionaries with response payload

"""
def get_public_bitso_api(api_name, params=None):
    available_apis = ["available_books", "ticker", "order_book", "trades"]

    if api_name not in available_apis:
        return None

    api_url = "{}{}/".format(bitso_api_url, api_name)

    print(api_name, params)

    response = requests.get(api_url, params)
    response_json = response.json()

    if (response_json['success'] == True):
        payload = response_json['payload']
    else:
        print("Error found in the request {}".format(response_json['error']))
        return None

    return payload
