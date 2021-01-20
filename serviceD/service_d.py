import flask
import logging

import worker


log = logging.getLogger(__name__)

app = flask.Flask(__name__)


@app.route("/health")
def handle_health():
    """Report the HTTP server health."""
    return flask.jsonify(status="up")


@app.route("/serv")
def handle_serv():
    """Compute some values."""
    if "X-Request-ID" in flask.request.headers:
        flask.g.request_id = flask.request.headers["X-Request-ID"]

    log.info("Service D /serv called")

    log.info("Creating Worker object ...")
    w = worker.Worker()
    log.info("Successfully created a Worker object")

    log.info("Initiating computation ...")
    w.compute()
    log.info("Successfully computed data")

    return flask.jsonify(service_d=w.data)


log.info("The Service E is ready and waiting for requests")
