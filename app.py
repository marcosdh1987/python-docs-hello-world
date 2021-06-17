from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def hello2():
    return "I'm a prediction"
