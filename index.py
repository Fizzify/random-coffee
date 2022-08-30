from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_random_coffee():
    url = "https://coffee.alexflipnote.dev/random.json"
    response = json.loads(requests.request("GET", url).text)

    file = response["file"]
    return file


@app.route("/")
def index():
    file_url = get_random_coffee()
    return render_template("index.html", coffee_url=file_url)


app.run(host="0.0.0.0", port=80)
