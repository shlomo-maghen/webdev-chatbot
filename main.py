from flask import Flask
import david
app = Flask(__name__)



@app.route("/")
def chatbot():
	display_chat_message(david.introduction())
	return david.introduction()

if __name__ == "__main__":
    app.run()