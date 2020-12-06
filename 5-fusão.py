import cv2
import numpy
import cv2

imagem1 = cv2.imread("ff16.jpg")
imagem2 = cv2.imread("ff162.jpg")
imagem1altura,imagem1largura, _ = imagem1.shape
imagem2 = cv2.resize(imagem2,(imagem1largura,imagem1altura))
fusao = cv2.addWeighted(imagem2,0.5,imagem1,0.5, 0)
cv2.imwrite("fffusao.jpg",fusao)
cv2.imshow("ffusao.jpg",fusao)
cv2.imshow("ff162.jpg",imagem2)
cv2.imshow("ff16.jpg",imagem1)
cv2.waitKey()

