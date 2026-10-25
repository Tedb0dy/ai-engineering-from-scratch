from flask import Flask
import torch

app = Flask(__name__)          # create the web app

@app.route("/")                # when someone visits http://.../  ...
def hello():                   # ...run this function...
    return {"message": "Hello from Docker", "torch": torch.__version__}
                               # ...and send this back. Flask turns a dict into JSON.

if __name__ == "__main__":     # only when this file is run directly:
    app.run(host="0.0.0.0", port=5000)   # start the server