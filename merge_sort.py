import random   # Para generar datos aleatorios simulando calificaciones
import time     # Para medir el tiempo de ejecución del algoritmo

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
# FUNCIÓN AUXILIAR: FUSIÓN DE LISTAS
# -----------------------------
def merge(left, right):
    """
    Fusiona dos listas ordenadas en una sola lista ordenada.
    """
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
# FUNCIÓN PARA MEDIR EL TIEMPO Y MOSTRAR RESULTADOS
# -----------------------------
def prueba_tiempos(n):
    """
    Genera n datos aleatorios, ordena usando merge_sort y mide el tiempo.
    Además, muestra los primeros 20 valores ordenados.
    """
    # Generar n datos únicos aleatorios
    datos = random.sample(range(1, 1000000), n)

    # Medir tiempo de inicio
    inicio = time.perf_counter()

    # Ordenar los datos
    ordenados = merge_sort(datos)

    # Medir tiempo de finalización
    fin = time.perf_counter()

    # Mostrar resultados
    print(f"\n--- Tamaño de datos: {n} ---")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
    print(f"Primeros 20 valores ordenados: {ordenados[:20]}")

    # Retornar tiempo para análisis de crecimiento
    return fin - inicio


# -----------------------------
# PRUEBA COMPARATIVA PARA VARIOS TAMAÑOS
# -----------------------------
tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
tiempos = []

print("=== Comparativa de tiempos de Merge Sort ===")

# Ejecutar pruebas para cada tamaño
for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

# Mostrar relación de crecimiento
print("\n=== Relación de crecimiento ===")
for i in range(1, len(tamaños)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")