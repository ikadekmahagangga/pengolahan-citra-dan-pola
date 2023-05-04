# memanggil library opencv
import cv2
from cv2 import waitKey
# menyimpan gambar dengan fungsi imread dari OpenCV
img = cv2.imread("gambar/PDI-P-1.png")
# sesuaikan dengan nama file yang diunggah pada cell sebelumnya
# menampilkan gambar dengan fungsi cv2_imshow
cv2.imshow('PDI-P-1', img)
waitKey(0)
# lihat tipe data img. disimpan sebagai apa?
print(type(img))