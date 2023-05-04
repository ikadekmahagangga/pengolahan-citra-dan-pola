import cv2
import numpy as np
from matplotlib import pyplot as plt
from cv2 import waitKey
img = cv2.imread("gambar/PDI-P-1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gambar Bunga Grayscale', img)
histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()
h, w = img.shape[:2]
max_intensity = 255
for i in range(h):
    for j in range(w):
        a = img.item(i, j)
        b = max_intensity - a
    img.itemset((i, j), b)
    cv2.imshow('Gambar Hasil', img)
histr =cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histr)
plt.show()
waitKey(0)