from flask import Flask

app = Flask(__name__)

#routes
@app.route('/')
def helloworld():
    return "First flask app build"
