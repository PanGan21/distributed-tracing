
"""The Gamma web service."""

import service_c
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = service_c.app
