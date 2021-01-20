import os
import flask
import logging
import requests

import utils

log = logging.getLogger(__name__)
app = flask.Flask(__name__)

service_b_endpoint = os.environ.get("SERVICE_B_ENDPOINT", None)
service_c_endpoint = os.environ.get("SERVICE_C_ENDPOINT", None)
if not service_c_endpoint or not service_b_endpoint:
    raise RuntimeError("Set the ENDPOINTS in environment variable")


@app.before_request
def before_request():
    """Generate a unique request ID."""
    flask.g.request_id = utils.generate_request_id()


@app.after_request
def after_request(response):
    """Return the unique request ID."""
    response.headers["Request_ID"] = flask.g.request_id
    return response


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/foo", methods=["POST"])
def handle_foo():
    """Invoke serviceB and then serviceC."""
    log.info("Service A /foo called")

    data = {}

    data.update({"foo": "111"})

    log.info("Sending request to Service B")
    resp = requests.post("%s/bar" % service_b_endpoint,
                         headers={"X-Request-ID": flask.g.request_id})
    log.info("Service B responded with status code %s and data `%s`",
             resp.status_code, resp.json())

    data.update(resp.json())

    log.info("Sending request to Service C")
    resp = requests.post("%s/spam" % service_c_endpoint,
                         headers={"X-Request-ID": flask.g.request_id})
    log.info("Service C responded with status code %s and data `%s`")

    data.update(resp.json())

    log.info("The overall response is `%s'", data)

    return flask.jsonify(data=data)


log.info("The Service A is ready and waiting for requests")
