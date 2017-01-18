from flask import Flask
from flask import render_template
import david
app = Flask(__name__)



@app.route("/")
def chatbot():

	return render_template("chatbot.html", name="shlomo")

def test():
	print 'ran'
	
if __name__ == "__main__":
    app.run()