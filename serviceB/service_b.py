import flask
import logging
import requests


log = logging.getLogger(__name__)

app = flask.Flask(__name__)


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/bar", methods=["POST"])
def handle_bar():
    """Get some data from the internet."""
    if "X-Request-ID" in flask.request.headers:
        flask.g.request_id = flask.request.headers["X-Request-ID"]

    log.info("Service B /bar called")

    log.info("Requesting data from the internet ...")
    resp = requests.get("https://www.githubstatus.com/")
    log.info("The external request status code is %s", resp.status_code)

    return flask.jsonify(bar="bar")


log.info("The Service B is ready and waiting for requests")
