"""The Service B."""

import service_b
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = service_b.app
