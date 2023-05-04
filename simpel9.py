import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load image
img = cv2.imread('gambar/PDI-P-1.png')
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Define ROI (Region of Interest)
roi = gray[100:500, 100:500]
# Calculate histogram
hist = cv2.calcHist([roi], [0], None, [256], [0, 256])
# Display histogram
plt.plot(hist)
# Show the plot
plt.show()
# Pada contoh di atas, kita mengimpor cv2 untuk memuat dan memproses gambar, serta numpy dan matplotlib.pyplot untuk menghitung dan menampilkan histogram. Selanjutnya, kita memuat gambar dari file dengan menggunakan cv2.imread('nama_file_gambar.png'). Kemudian, kita mengonversi gambar ke grayscale dengan menggunakan cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).
# Selanjutnya, kita mendefinisikan ROI (Region of Interest) sebagai segmen dari gambar grayscale dengan menggunakan gray[100:500, 100:500]. ROI ini akan digunakan sebagai input untuk menghitung histogram.
# Kemudian, kita menghitung histogram dari ROI menggunakan cv2.calcHist([roi], [0], None, [256], [0, 256]). Fungsi ini akan menghitung histogram dari data numerik dalam ROI menggunakan 256 interval (0-255).
# Setelah itu, kita menampilkan histogram menggunakan plt.plot(hist). Terakhir, kita menampilkan histogram dengan menggunakan plt.show().
# Semoga contoh di atas dapat memberikan gambaran tentang bagaimana menampilkan histogram dari data numerik pada segmen gambar.