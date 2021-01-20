"""The Service D."""

import service_d
import utils


utils.configure_logging()

# "Export" the app, so that gunicorn can find it
app = service_d.app
