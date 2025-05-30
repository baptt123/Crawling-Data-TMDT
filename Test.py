import cv2 as cv
import numpy as np
import os


# Notch filter
def createSpectrum(Fuv):
    spectrum = np.log1p(np.abs(Fuv))
    min = spectrum.min()
    max = spectrum.max()
    spectrum = 255 * (spectrum - min) / (max - min)
    return np.clip(spectrum, 0, 255).astype(np.uint8)





def createNotchFilter(shape, points, d0):
    H = np.ones(shape, dtype=np.uint8)
    cx=shape[0]//2
    cy=shape[1]//2
    for d in len(points):
        x = points[d][0]
        y = points[d][1]
        cv.circle(H, (x, y), d0, 0, -1)
        x1=x+2*(cx-x)
        y1=y+2*(cy-y)
        cv.circle(H, (x1, y1), d0, 0, -1)
    return H


# os.chdir("D:\WebScrapingPython\Test")
file = 'images.jpg'
img = cv.imread(file)
Fuv = np.fft.fft2(img)
Fuv = np.fft.fftshift(Fuv)
spectrum = createSpectrum(Fuv)
cv.imwrite("Spectrum.jpg", spectrum)

points=[[251,251],[240,256]]
d0=1
H = createNotchFilter(img.shape, points, d0)

G=Fuv*H
g=np.fft.ifftshift(G)
g=np.fft.ifft2(g)

out=np.real(g)
out=np.clip(out,0,255).astype(np.uint8)
cv.imshow('Orginal', img)
cv.imshow('G', G)
cv.imshow('Out', out)
cv.imshow("Notch", H=255)
cv.waitKey(0)
cv.destroyAllWindows()