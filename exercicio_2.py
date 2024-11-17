import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("imagem.png")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Exibir histograma de pixels imagem colorida
plt.hist(imagem.ravel(), bins = 256, range = [0,256])
plt.show()

print(imagem.shape)