from scipy import interpolate
from matplotlib import pyplot as plt
import numpy as np

class splineDrawer():
    def __init__(self, imgPath, t, c, k):
        self.imagePath = imgPath
        self.t = t
        self.c = c
        self.k = k

    def drawSpline(self):
        img = plt.imread(self.imagePath)
        fig, ax = plt.subplots()
        imgPlot = ax.imshow(img)
        spl = interpolate.BSpline(self.t, self.c, self.k)
        xx = [i for i in range(0, img.shape[1], 50)]
        ax.plot(xx, spl(xx), 'b-', lw=4, alpha=0.7, label='BSpline')
        ax.grid(True)
        ax.legend(loc='best')
        plt.show()
