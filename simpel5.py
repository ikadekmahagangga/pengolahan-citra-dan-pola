import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("gambar/lena.jpg")
cv2.imshow('Gambar Asli', img)
waitKey(0)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
brightness = 50
h, w = img2.shape[:2]
for i in np.arange(h):
 for j in np.arange(w):
 a = img2.item(i, j)
 b = a + brightness
 if b > 255:
     for i in np.arange(h):
 for j in np.arange(w):
    a = img2.item(i, j)
     b = a + brightness
 if b > 255: