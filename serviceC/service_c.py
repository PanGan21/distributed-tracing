import os
import flask
import logging
import requests


log = logging.getLogger(__name__)

app = flask.Flask(__name__)

service_d_endpoint = os.environ.get("SERVICE_D_ENDPOINT", None)
if not service_d_endpoint:
    raise RuntimeError("Set the ENDPOINT environment variable")


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/spam", methods=["POST"])
def handle_spam():
    """Get some data from delta."""
    if "X-Request-ID" in flask.request.headers:
        flask.g.request_id = flask.request.headers["X-Request-ID"]

    log.info("Service C /spam called")

    log.info("Requesting data from Service D")
    resp = requests.get("%s/serv" % service_d_endpoint,
                        headers={"X-Request-ID": flask.g.request_id})
    log.info("Service D responded with status code %s and data `%s'",
             resp.status_code, resp.json())

    return flask.jsonify(spam=["cats", "dogs"], delta=resp.json())
    return 0


log.info("The Service C is ready and waiting for requests")
