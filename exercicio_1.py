import cv2
import matplotlib.pyplot as plt

# Lendo uma imagem
#imagem = cv2.imread("imagem.png")
#imagem = cv2.imread("imagem.png", cv2.IMREAD_COLOR) # Cor
#imagem = cv2.imread("imagem.png", cv2.IMREAD_GRAYSCALE) # Cinza
imagem = cv2.imread("imagem.png", cv2.IMREAD_UNCHANGED) # Canal Alpha

# Mostrando imagem
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(2000)

# Console L,A,C,T
print("Largura (w) %d pixels" % (imagem.shape[1]))
print("Altura (h) %d pixels" % (imagem.shape[0]))
print("Canais %d " % (imagem.shape[2]))
print("Tipo: ", imagem.dtype)

# Salvar nova imagem
cv2.imwrite("nova_imagem.png", imagem)

# Transformar nova imagem em RGB
imagem2 = cv2.imread("nova_imagem.png")
imagem2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2RGB)

# Mostrando imagem
cv2.imshow('Nova imagem em RGB', imagem2)
cv2.waitKey(2000)

# Imagem HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HLS)

# Mostrando imagem
cv2.imshow('Imagem HLS', imagem_hsv)
cv2.waitKey(2000)

# Imagem Matiz
imagem_Matiz = imagem_hsv[:,:,0]

# Mostrando imagem
cv2.imshow('Imagem Matiz', imagem_Matiz)
cv2.waitKey(2000)