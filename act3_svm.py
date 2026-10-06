import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Datos: [energia de la guitarra, distorsion de la guitarra]
X = np.array([
    [3, 1], [4, 2], [5, 2], [6, 3],      # Pop
    [7, 7], [8, 7], [9, 8], [10, 9]      # Rock
])

# 0 = Pop, 1 = Rock
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Crear y entrenar la SVM
modelo = svm.SVC(kernel="linear", C=10)
modelo.fit(X, y)

# Nueva canción: energia, distorsion
cancion = np.array([[7, 5]])
prediccion = modelo.predict(cancion)

print("=== CLASIFICADOR MUSICAL SVM ===")
print("Energia:", cancion[0][0])
print("Distorsion:", cancion[0][1])

if prediccion[0] == 0:
    print("Genero predicho: POP")
else:
    print("Genero predicho: ROCK")

print("Precision:", modelo.score(X, y) * 100, "%")

# Graficar los datos
plt.scatter(X[y == 0, 0], X[y == 0, 1], s=100, label="Pop")
plt.scatter(X[y == 1, 0], X[y == 1, 1], s=100, label="Rock")
plt.scatter(cancion[0][0], cancion[0][1],
            s=200, marker="*", label="Nueva cancion")

# Frontera de decision
w = modelo.coef_[0]
b = modelo.intercept_[0]
x = np.linspace(2, 11, 100)
y_line = -(w[0] * x + b) / w[1]

plt.plot(x, y_line, label="Frontera SVM")

plt.title("Clasificacion musical con SVM")
plt.xlabel("Energia")
plt.ylabel("Distorsion")
plt.grid()
plt.legend()
plt.show()