import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# BUBBLE SORT
# -----------------------------
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# -----------------------------
# MERGE SORT
# -----------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

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
# QUICK SORT
# -----------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# -----------------------------
# MEDIR TIEMPO
# -----------------------------
def medir_tiempo(funcion, datos):
    inicio = time.perf_counter()
    funcion(datos)
    fin = time.perf_counter()
    return fin - inicio


# -----------------------------
# TAMAÑOS DE PRUEBA
# -----------------------------
tamaños = [2000, 5000, 10000, 20000]

tiempos_bubble = []
tiempos_merge = []
tiempos_quick = []

print("=== Comparativa de algoritmos de ordenamiento ===")

for n in tamaños:

    datos = random.sample(range(1, 1000000), n)

    print(f"\nTamaño de datos: {n}")

    # Bubble
    t = medir_tiempo(bubble_sort, datos.copy())
    tiempos_bubble.append(t)
    print(f"Bubble Sort: {t:.6f} s")

    # Merge
    t = medir_tiempo(merge_sort, datos.copy())
    tiempos_merge.append(t)
    print(f"Merge Sort: {t:.6f} s")

    # Quick
    t = medir_tiempo(quick_sort, datos.copy())
    tiempos_quick.append(t)
    print(f"Quick Sort: {t:.6f} s")


# -----------------------------
# GRÁFICA COMPARATIVA
# -----------------------------
plt.figure(figsize=(9,6))

plt.plot(tamaños, tiempos_bubble, marker='o', label="Bubble Sort")
plt.plot(tamaños, tiempos_merge, marker='o', label="Merge Sort")
plt.plot(tamaños, tiempos_quick, marker='o', label="Quick Sort")

plt.title("Comparación de algoritmos de ordenamiento")
plt.xlabel("Cantidad de datos")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid(True)

plt.show()