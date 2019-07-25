import os
import requests
import time
from flask import Flask, render_template
from pusher import Pusher

app = Flask(__name__)

PUSHER_APP_ID = os.environ.get("pusher_app_id")
PUSHER_KEY = os.environ.get("pusher_key")
PUSHER_SECRET = os.environ.get("pusher_secret")

pusher = Pusher(
    app_id=PUSHER_APP_ID,
    key=PUSHER_KEY,
    secret=PUSHER_SECRET,
    cluster="eu",
    ssl=True
)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
