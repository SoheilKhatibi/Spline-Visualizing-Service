from flask import Flask

flaskApp = Flask(__name__)

@flaskApp.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    flaskApp.run()
