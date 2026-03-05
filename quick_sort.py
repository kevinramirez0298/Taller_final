import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# FUNCIÓN QUICK SORT
# -----------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# -----------------------------
# FUNCIÓN PARA MEDIR TIEMPO
# -----------------------------
def prueba_tiempos(n):
    datos = random.sample(range(1, 1000000), n)

    inicio = time.perf_counter()
    ordenados = quick_sort(datos)
    fin = time.perf_counter()

    print(f"\n--- Tamaño de datos: {n} ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Primeros 20 valores ordenados: {ordenados[:20]}")

    return fin - inicio

# -----------------------------
# PRUEBA PARA VARIOS TAMAÑOS
# -----------------------------
tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
tiempos = []

print("=== Comparativa de tiempos Quick Sort ===")

for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

# -----------------------------
# RELACIÓN DE CRECIMIENTO
# -----------------------------
print("\n=== Relación de crecimiento aproximada ===")
for i in range(1, len(tiempos)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")

# -----------------------------
# GRÁFICA DE RESULTADOS
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(tamaños, tiempos, marker='o', color='blue')

plt.title("Tiempo de ejecución de Quick Sort")
plt.xlabel("Cantidad de datos")
plt.ylabel("Tiempo (segundos)")
plt.grid(True)

plt.show()