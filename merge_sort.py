import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# FUNCIÓN MERGE SORT
# -----------------------------
def merge_sort(arr):
    """
    Merge Sort ordena una lista usando Divide y Vencerás.
    Complejidad: O(n log n) en todos los casos.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# -----------------------------
# FUNCIÓN AUXILIAR: MERGE
# -----------------------------
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -----------------------------
# FUNCIÓN PARA MEDIR TIEMPOS
# -----------------------------
def prueba_tiempos(n):
    datos = random.sample(range(1, 1000000), n)

    inicio = time.perf_counter()
    ordenados = merge_sort(datos)
    fin = time.perf_counter()

    print(f"\n--- Tamaño de datos: {n} ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Primeros 20 valores ordenados: {ordenados[:20]}")

    return fin - inicio

# -----------------------------
# PRUEBA COMPARATIVA
# -----------------------------
tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
tiempos = []

print("=== Comparativa de tiempos de Merge Sort ===")

for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

# -----------------------------
# RELACIÓN DE CRECIMIENTO
# -----------------------------
print("\n=== Relación de crecimiento ===")
for i in range(1, len(tamaños)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")

# -----------------------------
# GRÁFICA
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(tamaños, tiempos, marker='o', color='green')

plt.title("Tiempo de ejecución de Merge Sort")
plt.xlabel("Cantidad de datos")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)

plt.show()