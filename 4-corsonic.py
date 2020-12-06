import numpy
import cv2

imagem = cv2.imread("sonic.jpg")

for y in range(0,imagem.shape[0]):
    for x in range(1,imagem.shape[1]):
        if imagem[y][x][0] > 100 and imagem[y][x][0] < 255 and imagem[y][x][1] and imagem[y][x][2] < 104:
                imagem[y][x][0] = 0
                imagem[y][x][1] = 100
                imagem[y][x][2] = 0
cv2.imwrite("imagem.jpg",imagem)
cv2.imshow("imagem.jpg",imagem)
cv2.waitKey()