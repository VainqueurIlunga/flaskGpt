from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Bienvenue sur flask</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.01', port=5000)