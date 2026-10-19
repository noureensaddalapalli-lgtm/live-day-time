

from flask import Flask, render_template
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/time")
def get_time():
    now = datetime.now(ZoneInfo("Asia/Kolkata"))

    return {
        "day": now.strftime("%A"),
        "date": now.strftime("%d %B %Y"),
        "time": now.strftime("%I:%M:%S %p"),
        "timezone": "India Standard Time"
    }


if __name__ == "__main__":
    app.run(debug=True)
