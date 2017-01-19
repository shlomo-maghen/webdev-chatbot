from flask import Flask
from flask import render_template
from flask import request
import david
app = Flask(__name__)


@app.route("/")
def chatbot():
	return render_template("index2.html")


@app.route("/get_response/", methods=["GET", "POST"])
def get_response():
	json_object = request.get_json(force=True)
	return david.get_element(json_object)


if __name__ == "__main__":
    app.run()