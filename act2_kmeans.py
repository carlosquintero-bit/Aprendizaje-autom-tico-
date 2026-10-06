import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Datos
datos = np.array([
    [1, 8],
    [2, 7],
    [1, 9],
    [2, 8],
    [7, 2],
    [8, 1],
    [9, 2],
    [8, 3],
    [5, 5],
    [6, 4]
])

# 2. Crear el modelo K-Means
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)

# 3. Entrenar el modelo
kmeans.fit(datos)

# 4. Obtener el grupo de cada persona
grupos = kmeans.labels_

# 5. Obtener los centros de los grupos
centros = kmeans.cluster_centers_

# 6. Mostrar resultados
print("Grupo de cada persona:")
print(grupos)

print("\nCentros de los grupos:")
print(centros)

# 7. Graficar los resultados
plt.scatter(datos[:, 0], datos[:, 1], c=grupos)

# Mostrar los centros
plt.scatter(
    centros[:, 0],
    centros[:, 1],
    marker="X",
    s=200
)

plt.xlabel("Horas de ejercicio por semana")
plt.ylabel("Horas de videojuegos por semana")
plt.title("Agrupación usando K-Means")
plt.show()