
import cv2

def recolorir(imagem,cor):
  copia=imagem.copy()
  if cor == "vermelho":
    copia[:, :, 0] = 0
    copia[:, :, 1] = 0
  elif cor =="verde":
    copia[:, :, 0] = 0
    copia[:, :, 2] = 0
  elif cor == "azul":
    copia[:, :, 1] = 0
    copia[:, :, 2] = 0
  else:
    return 0
  return copia

def media_de_cor(imagem):
  tamanho = imagem.shape
  soma=0
  print(tamanho)
  for i in range(0,tamanho[0]):
    for j in range(0,tamanho[1]):
      for k in range(0,tamanho[2]):
          soma+=imagem[i,j,k]
  return soma

def quantidade_de_cor(imagem):
  cores=[["vermelho",0],["verde",0],["azul",0]]
  for i in cores:
    cor_da_imagem = recolorir(imagem, i[0])
    cv2.imwrite("cor.jpg",cor_da_imagem)
    cv2.imshow("cor.jpg",cor_da_imagem)
    i[1]=media_de_cor(cor_da_imagem)
    print(i)
  resultado=["",0]
  for i in cores:
    print(i)
    if resultado[0] != i[0] and resultado[1]<i[1]:
      print(resultado)
      resultado = i
  return resultado

imagem_jogador = cv2.imread("6QscS.jpg")
cv2.imshow("messicor",imagem_jogador)
print("cor mais presente: ", quantidade_de_cor((imagem_jogador)))
cv2.waitKey()