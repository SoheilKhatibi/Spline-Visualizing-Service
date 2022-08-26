from scipy import interpolate
from matplotlib import pyplot as plt
import numpy as np
import os

class splineDrawer():
    def __init__(self, imgPath, t, c, k):
        self.imagePath = imgPath
        self.t = t
        self.c = c
        self.k = k

    def drawSpline(self, resultDir):
        img = plt.imread(self.imagePath)
        print(img.shape)
        fig, ax = plt.subplots()
        imgPlot = ax.imshow(img)
        spl = interpolate.BSpline(self.t, self.c, self.k)
        xx = [i for i in range(0, img.shape[1], 50)]
        ax.plot(xx, spl(xx), 'b-', lw=4, alpha=0.7, label='BSpline')
        ax.grid(True)
        ax.legend(loc='best')
        plt.savefig(os.path.join(resultDir, 'result.png'), bbox_inches='tight', pad_inches=0, dpi=300)
