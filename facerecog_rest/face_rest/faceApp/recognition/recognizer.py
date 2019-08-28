
# Imports
import argparse
import imutils
import cv2
from sklearn.neural_network import MLPClassifier
#from sklearn.neighbors import KNeighborsClassifier
from skimage import exposure
from skimage import feature
from imutils import paths


def Recognizer(image):
	# Inicializa a matriz de dados e de labels
	print("Extraindo recursos...")
	data = []
	labels = []

	# Loop pelas imagens no dataset de treino
	for imagePath in paths.list_images('/home/philipe/PycharmProjects/RecogKNN/fotos_treino'):
		make = imagePath.split("/")[-2]
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# edged = imutils.auto_canny(gray)

		# Encontra contornos no mapa de borda, mantendo apenas o maior que se supõe ser o logotipo do carro
		cnts, hierarchy = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		c = max(cnts, key=cv2.contourArea)

		# Extrai o logotipo do carro e redimensiona
		(x, y, w, h) = cv2.boundingRect(c)
		logo = gray[y:y + h, x:x + w]
		logo = cv2.resize(logo, (200, 100))

		# Extrai Histograma de Gradientes Orientados do logotipo
		# Os parâmetros mais importantes para o descritor HOG são: orientations, pixels_per_cell e cells_per_block.
		# Esses três parâmetros (juntamente com o tamanho da imagem de entrada) controlam efetivamente a dimensionalidade
		# do vetor de características resultante.
		H = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2), transform_sqrt=True)

		# Atualiza dados e labels
		data.append(H)
		labels.append(make)

	# Treina o Classificador Nearest Neighbors
	print("Treinando o Classificador...")

	# Cria o modelo
	model = MLPClassifier(hidden_layer_sizes=(100,), activation="relu", solver='adam')

	# Fit do modelo
	model.fit(data, labels)

	# Cria o classificador
	classificador = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

	# Loop no dataset de teste
	print("Avaliando...")
	for (i, imagePath) in enumerate(paths.list_images('/media')):
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		logo = cv2.resize(gray, (200, 100))

		# Extrai o Histograma de Gradientes Orientados da imagem de teste e prevê a marca do carro
		(H, hogImage) = feature.hog(logo, orientations=9, pixels_per_cell=(10, 10), cells_per_block=(2, 2),
									transform_sqrt=True, visualize=True)
		pred = model.predict(H.reshape(1, -1))[0]

		# Visualiza a imagem HOG
		# hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
		# hogImage = hogImage.astype("uint8")
		# cv2.imshow("HOG Image #{}".format(i + 1), hogImage)

		# Print das previsões
		cv2.putText(image, pred.title(), (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
		print(pred.title())


