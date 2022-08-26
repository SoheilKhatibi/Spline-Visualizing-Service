from flask import Flask, request, render_template
import os

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


if __name__ == '__main__':
    flaskApp.run()
