import threading

from flask import Flask
from flask import request
from functools import wraps

# Main Flask app where endpoints will be dynamically registered
app = Flask(__name__)


def expose(path):
    """Register an endpoint to excute the given function."""

    def register_endpoint(function):

        @wraps(function)
        def view(*args, **kwargs):
            """Target Flask view to handle API requests."""
            return str(function(**request.args))
        app.route(path)(view)

        # Return the unmodified decorated function
        return function

    return register_endpoint


thread = threading.Thread(target = app.run)
thread.setdaemon = True
thread.start()
