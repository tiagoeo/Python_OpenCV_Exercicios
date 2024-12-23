import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("imagem.png")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Exibir histograma de pixels imagem colorida
plt.hist(imagem.ravel(), bins = 256, range = [0,256])
plt.show()

print(imagem.shape)

# Negativo da imagem
for i in range(786):
    for j in range(762):
        imagem[i,j]=255-imagem[i,j]
cv2.imwrite('imagem2.png', imagem)
imagem2 = cv2.imread('imagem2.png')
cv2.imshow('Imagem Negativo', imagem)
cv2.waitKey(2000)

# Texto em Imagem
foto = cv2.imread("imagem.png", cv2.IMREAD_COLOR)
foto = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)
foto.shape
cv2.putText(foto, "Texto aqui!", (270,333), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
plt.imshow(foto)
plt.title('Inserindo texto em uma Imagem')
plt.show()