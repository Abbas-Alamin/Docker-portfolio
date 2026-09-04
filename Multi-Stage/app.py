from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello"

@app.route("/abbas")
def getdata():
    return "hello it's abbas"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
