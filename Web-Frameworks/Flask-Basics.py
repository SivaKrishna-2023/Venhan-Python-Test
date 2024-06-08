from flask import Flask  # type: ignore

app = Flask(__name__)

@app.route("/")

def home():
    return "<h1>Welcome toFlask!</h1>"


if __name__ == "__main__":
    app.run()