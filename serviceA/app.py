"""The Service A."""

import service_a
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = service_a.app
