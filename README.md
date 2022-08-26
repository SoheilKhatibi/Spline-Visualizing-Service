# Spline-Visualizing-Service

This is the implementation of a Flask server that illustrates B-Spline interpolation on an image.

## Inputs

Image file and tck parameters, where;

t: Stands for knots,
c: Stands for coefficients, and
k: Stands for degree

Also, ```Scipy.splrep``` can be used to calculate tck parameters for a cubic curve that passes through the given control points.


## Running

This repo is developed with python 3.9.5.

To run, simply do:
```
pip install -r requirements.txt
python main.py
```


## Reference
-HTML page design were inspired by [this link](<https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3> "link")

-[Sample image](<./resource/image/mountain_PNG12.png> "sample image") from pngimg.com website ([link](<https://pngimg.com/image/21592> "image link"))
