import json

from flask import (
    Flask,
    request,
    Response
)
from waitress import serve

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://af036de372754832a5402dccaf7a4ecd@o1167281.ingest.sentry.io/6258220",
    integrations=[FlaskIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def data():
    try:
        language = request.args.get("language")
        call_type = request.args.get("type")
    except:
        return "Invalid arguments", 200

    file_src = f'data/{language}/{call_type}.json'
    with open(file_src, "r", encoding='utf-8') as pack:
        response = json.load(pack)

    response = json.dumps(response)

    return Response(response, mimetype='application/json')


serve(app, host="0.0.0.0", port=8080)
