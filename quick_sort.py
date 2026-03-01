import random
import time

# -----------------------------
# FUNCIÓN QUICK SORT
# -----------------------------
def quick_sort(arr):
    """
    Ordena una lista usando Quick Sort (Divide y Vencerás):
    1. Elegir un pivote (último elemento).
    2. Colocar los elementos menores a la izquierda y mayores a la derecha.
    3. Ordenar recursivamente las sublistas izquierda y derecha.
    
    Complejidad:
        Mejor y promedio: O(n log n)
        Peor caso: O(n^2) (cuando la lista ya está ordenada y se elige el último elemento como pivote)
    """
    if len(arr) <= 1:
        return arr

    # Elegir pivote (último elemento)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores o iguales al pivote
    right = [x for x in arr[:-1] if x > pivot]  # Elementos mayores al pivote

    # Ordenar recursivamente izquierda y derecha, luego combinar
    return quick_sort(left) + [pivot] + quick_sort(right)

# -----------------------------
# FUNCIÓN PARA MEDIR TIEMPO Y MOSTRAR RESULTADOS
# -----------------------------
def prueba_tiempos(n):
    """
    Genera n datos aleatorios y los ordena usando Quick Sort.
    Mide tiempo de ejecución y muestra los primeros 20 valores ordenados.
    """
    datos = random.sample(range(1, 1000000), n)
    
    inicio = time.perf_counter()
    ordenados = quick_sort(datos)
    fin = time.perf_counter()
    
    print(f"\n--- Tamaño de datos: {n} ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Primeros 20 valores ordenados: {ordenados[:20]}")
    
    return fin - inicio

# -----------------------------
# PRUEBA COMPARATIVA PARA VARIOS TAMAÑOS
# -----------------------------
tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
tiempos = []

print("=== Comparativa de tiempos Quick Sort ===")

for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

# Relación de crecimiento aproximada
print("\n=== Relación de crecimiento aproximada ===")
for i in range(1, len(tiempos)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")