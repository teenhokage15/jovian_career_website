from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello World"

print(__name__)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host = '0.0.0.0', debug = True)

