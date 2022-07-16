import json

from flask import (
    Flask,
    request,
    Response
)
from waitress import serve

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def data():
    try:
        language = request.args.get("language")
        call_type = request.args.get("type")

        file_src = f'data/{language}/{call_type}.json'
        with open(file_src, "r", encoding='utf-8') as pack:
            response = json.load(pack)
    
        response = json.dumps(response)

        return Response(response, mimetype='application/json')

    except:
        return "Invalid arguments", 200

serve(app, host="0.0.0.0", port=8080)
