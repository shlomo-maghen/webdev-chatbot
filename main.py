from flask import Flask
from flask import render_template
import david
app = Flask(__name__)


@app.route("/")
def chatbot():
	return render_template("chatbot.html")


@app.route("/get_response/<sentence>")
def get_response(sentence):
	return david.get_element(sentence)	

if __name__ == "__main__":
    app.run()