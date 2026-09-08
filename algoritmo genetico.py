import random

# Puntos de cada ingrediente
puntos = [4, 5, 3, 2]

# Tamaño de la población
tam_poblacion = 6

# Número de generaciones
generaciones = 10

# Probabilidad de mutación
prob_mutacion = 0.1


# -------------------------------
# 1. Crear una pizza aleatoria
# -------------------------------
def crear_pizza():
    return [random.randint(0, 1) for _ in range(4)]


# -------------------------------
# 2. Función objetivo
# -------------------------------
def evaluar(pizza):
    total = 0

    for i in range(4):
        total += pizza[i] * puntos[i]

    return total


# -------------------------------
# 3. Crear población
# -------------------------------
poblacion = []

for i in range(tam_poblacion):
    poblacion.append(crear_pizza())


# -------------------------------
# 4. Algoritmo genético
# -------------------------------
for generacion in range(generaciones):

    # Ordenar de mejor a peor
    poblacion.sort(key=evaluar, reverse=True)

    # Seleccionar las 2 mejores
    padre1 = poblacion[0]
    padre2 = poblacion[1]

    nueva_poblacion = [padre1, padre2]

    # Crear nuevos hijos
    while len(nueva_poblacion) < tam_poblacion:

        # Cruzamiento
        hijo = padre1[:2] + padre2[2:]

        # Mutación
        for i in range(4):
            if random.random() < prob_mutacion:
                hijo[i] = 1 - hijo[i]

        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

    # Mostrar mejor pizza
    mejor = max(poblacion, key=evaluar)

    print(
        "Generación:", generacion + 1,
        "Pizza:", mejor,
        "Puntos:", evaluar(mejor)
    )


# -------------------------------
# 5. Mostrar resultado final
# -------------------------------
mejor = max(poblacion, key=evaluar)

print("\nMEJOR PIZZA")
print("Ingredientes:", mejor)
print("Puntuación:", evaluar(mejor))