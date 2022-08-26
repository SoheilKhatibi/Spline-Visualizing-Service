from flask import Flask, request, render_template
import os
import inputParser
from splineDrawer import splineDrawer

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

flaskApp = Flask(__name__)
flaskApp.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@flaskApp.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@flaskApp.route('/setInputs', methods=['POST', 'GET'])
def setInputs():
    """
    Set inputs of the algorithm
    """
    if request.method == "POST":
        image = request.files["image"]
        if not image:
            return 'No image was uploaded', 400
        else:
            image.save(os.path.join(flaskApp.config['UPLOAD_FOLDER'], image.filename))
            return render_template("setInputs.html", user_image=image.filename)

@flaskApp.route('/infer', methods=['POST', 'GET'])
def infer():
    """
    """

    t = request.form['T']
    c = request.form['C']
    k = request.form['K']
    fileName = request.form['name'][:-1]

    t = inputParser.parseTValues(t)

    c = inputParser.parseCValues(c)

    k = inputParser.parseKValue(k)

    imagePath = os.path.join(flaskApp.config['UPLOAD_FOLDER'], fileName)

    drawer = splineDrawer(imagePath, t, c, k)

    drawer.drawSpline(flaskApp.config['UPLOAD_FOLDER'])

    return render_template('result.html', user_image='result.png')

if __name__ == '__main__':
    flaskApp.run()
