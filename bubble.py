import random   # Para generar datos aleatorios simulando calificaciones
import time     # Para medir el tiempo de ejecución del algoritmo

# -----------------------------
# FUNCIÓN BUBBLE SORT
# -----------------------------
def bubble_sort(arr):
    """
    Bubble Sort ordena una lista comparando elementos adyacentes
    y moviendo los mayores hacia el final.
    Complejidad:
        Mejor caso: O(n)
        Peor y promedio: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# -----------------------------
# FUNCIÓN PARA MEDIR EL TIEMPO Y MOSTRAR RESULTADOS
# -----------------------------
def prueba_tiempos(n):
    """
    Genera n datos aleatorios, ordena usando bubble_sort y mide el tiempo.
    Además, muestra los primeros 20 valores ordenados.
    """
    datos = random.sample(range(1, 1000000), n)

    inicio = time.perf_counter()
    ordenados = bubble_sort(datos)
    fin = time.perf_counter()

    print(f"\n--- Tamaño de datos: {n} ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Primeros 20 valores ordenados: {ordenados[:20]}")

    return fin - inicio

# -----------------------------
# PRUEBA COMPARATIVA PARA VARIOS TAMAÑOS
# -----------------------------
tamaños = [2000, 10000, 20000]  # Para Bubble Sort grandes tamaños tardan demasiado
tiempos = []

print("=== Comparativa de tiempos de Bubble Sort ===")
for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

print("\n=== Relación de crecimiento ===")
for i in range(1, len(tamaños)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")