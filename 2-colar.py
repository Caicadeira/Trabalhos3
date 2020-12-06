import numpy
import cv2

def crop(img,x_ini,y_ini,largura_x,altura_y):
  return img[y_ini:y_ini+altura_y, x_ini:x_ini+largura_x]

imagem= cv2.imread("6QscS.jpg")
x_bola = 334
y_bola = 287
largura_bola = 56
altura_bola = 49
ballImg = crop(imagem, x_bola, y_bola, largura_bola, altura_bola)
imagem[288 : 288 + ballImg.shape[0],150:150 + ballImg.shape[1]] = ballImg
cv2.imwrite("futbola.jpg",imagem)
cv2.imshow("futbola.jpg",imagem)