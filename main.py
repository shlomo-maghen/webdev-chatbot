from flask import Flask
import david
app = Flask(__name__)



@app.route("/")
def hello():
	# return "sdfsdfsdfsd"
	return david.introduction()

if __name__ == "__main__":
    app.run()