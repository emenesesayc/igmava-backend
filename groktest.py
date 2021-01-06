import os
import sys

from flask import Flask

def init_webhooks(base_url):
    # No tocar
    pass

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
    )

    if app.config.get("ENV") == "development" and app.config["USE_NGROK"]:
        from pyngrok import ngrok


        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000

        public_url = ngrok.connect(port).public_url
        print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))
        # esto deberia imprimir la nueva url pero  no llega, se queda pegado en el connect.
        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)
        # aunque no llega a ejecutarse esto igual funciona aparentemente.
    # Aqui las funciones
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app
