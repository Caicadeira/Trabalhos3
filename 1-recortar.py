import numpy
import cv2

def crop(img,x_ini,y_ini,largura_x,altura_y):
  return img[y_ini:y_ini+altura_y, x_ini:x_ini+largura_x]

messiImg= cv2.imread("6QscS.jpg")
x_bola = 334
y_bola = 287
largura_bola = 56
altura_bola = 49
ballImg = crop(messiImg, x_bola, y_bola, largura_bola, altura_bola)
cv2.imwrite("futbola.jpg",ballImg)
cv2.imshow("futbola.jpg",ballImg)