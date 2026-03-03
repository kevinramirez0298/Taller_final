#  Análisis de Algoritmos de Ordenamiento para Plataforma Académica

##  Descripción del Problema

En base a la necesidad del problema se requiere una plataforma de análisis académico para procesar diariamente los resultados de pruebas realizadas por estudiantes de todo el país.

El sistema debe ordenar las calificaciones de menor a mayor para generar:

- Reportes estadísticos
- Rankings
- Análisis comparativos

---

## Volumen de Datos

- Día normal: aproximadamente **2.000 registros**
- Convocatorias nacionales: entre **30.000 y 80.000 registros**

---

## Características del Sistema

- Los datos llegan en **orden aleatorio**
- El proceso de ordenamiento se ejecuta **varias veces al día**
- Se requiere un **tiempo de respuesta bajo**
- En algunos casos, los datos pueden estar **parcialmente ordenados**

---

# Análisis del Escenario

## Tamaño Potencial Máximo

El sistema puede llegar a procesar hasta **80.000 registros**, lo que representa un volumen considerable de datos.

## Tipo de Escenario

El escenario es:

- Variable (datos pequeños y grandes)
- De ejecución frecuente
- Sensible al tiempo de respuesta

## Requisitos del Algoritmo

El algoritmo seleccionado debe:

- Escalar eficientemente
- Mantener buen rendimiento en grandes volúmenes
- No degradarse significativamente
---

# Análisis de Algoritmos Disponibles

Los algoritmos disponibles son:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

---

## Comparación de Complejidades

| Algoritmo        | Mejor Caso | Promedio     | Peor Caso   | Escalabilidad |
|------------------|------------|--------------|-------------|---------------|
| Bubble Sort      | O(n)       | O(n²)        | O(n²)       | ❌ Baja       |
| Selection Sort   | O(n²)      | O(n²)        | O(n²)       | ❌ Baja       |
| Insertion Sort   | O(n)       | O(n²)        | O(n²)       | ⚠️ Limitada   |
| Merge Sort       | O(n log n) | O(n log n)   | O(n log n)  | ✅ Alta       |
| Quick Sort       | O(n log n) | O(n log n)   | O(n²)       | ✅ Muy Alta   |

---

# Análisis Individual

## Bubble Sort

- Realiza demasiadas comparaciones.
- Su complejidad es O(n²).
- Con 80.000 registros sería extremadamente lento.

**Conclusión:** No recomendado.

---

## Selection Sort

- Siempre trabaja en O(n²).
- No mejora si los datos están casi ordenados.

**Conclusión:** No recomendado.

---

## Insertion Sort

- Muy eficiente con datos pequeños o casi ordenados.
- En grandes volúmenes se degrada a O(n²).

**Conclusión:** Útil solo en conjuntos pequeños.

---

## Merge Sort

- Complejidad estable O(n log n).
- Muy eficiente en grandes volúmenes.
- Requiere memoria adicional.

**Conclusión:** Buena opción para grandes cantidades de datos.

---

## Quick Sort

- Complejidad promedio O(n log n).
- Muy rápido en la práctica.
- Bajo uso de memoria comparado con Merge.
- Puede evitar el peor caso usando pivote aleatorio.

**Conclusión:** Es el más eficiente en la mayoría de escenarios reales.

---
# Desicion Final

Por la eficiencia del algoritmo se considera más adecuado para esta plataforma, por su tiempo de respuesta y capacidad de ejecucion.  

## Quick Sort

### Justificación Técnica

- Escala eficientemente hasta 80.000 registros.
- Ofrece tiempos de respuesta bajos.
- Funciona bien con datos aleatorios.
- Es más rápido en la práctica que otros algoritmos O(n log n).
- Puede optimizarse para evitar el peor caso.

---
# Codigo en Python 

    import random
    import time

    ___________________________________
    *FUNCIÓN QUICK SORT*
    ___________________________________
    def quick_sort(arr):
    
    "Ordena una lista usando Quick Sort (Divide y Vencerás):
    1. Elegir un pivote (último elemento).
    2. Colocar los elementos menores a la izquierda y mayores a la derecha.
    3. Ordenar recursivamente las sublistas izquierda y derecha."
    
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


    *FUNCIÓN PARA MEDIR TIEMPO Y MOSTRAR RESULTADOS

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


    *PRUEBA COMPARATIVA PARA VARIOS TAMAÑOS

    tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
    tiempos = []

    print("=== Comparativa de tiempos Quick Sort ===")

    for n in tamaños:
    tiempo = prueba_tiempos(n)
    tiempos.append(tiempo)

    * Relación de crecimiento aproximada
    print("\n=== Relación de crecimiento aproximada ===")
    for i in range(1, len(tiempos)):
    factor = tiempos[i] / tiempos[i-1]
    print(f"{tamaños[i-1]} → {tamaños[i]} : tarda ~{factor:.2f} veces más")


# Relación de Crecimiento Aproximada 

2000 → 10000 : tarda ~4.01 veces más
10000 → 20000 : tarda ~1.61 veces más
20000 → 40000 : tarda ~2.32 veces más
40000 → 60000 : tarda ~1.44 veces más
60000 → 80000 : tarda ~1.56 veces más

---
# Funcionamiento de Codigo Python
    import random
    import time


Importaciones que se usan para aceder a librerias como random y time.
* **Random:** se usa para generar numeros aleatorios sin repetir
ejemplo: random.sample(range(1, 1000000), n).
* **Time:** se utiliza para medir el tiempo con alta precision ejemplo: time.perf_counter()
---

         def quick_sort(arr):

* Implementacion del algoritmo quick sort. 
---

         if len(arr) <= 1:
            return arr
* **Caso Base:** Si la lista tiene 0 o 1 elemento, la lista ya estaria ordenada.
---

        pivot = arr[-1]
* **Selecion de Pivote** se seleciona el ultimo elemento como pivote, el pivote es el valor que divide la lista.
---

        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

* **Division de la lista:** Se crean dos listas

* **left:** Elemntos menores o iguales al pivote.

* **right:** Elemtos mayores al pivote.
---

        return quick_sort(left) + [pivot] + quick_sort(right)

* **Recursividad:** se ordena la sublista izquierda, se coloca el pivote en el centro, se ordena la sublista derecha y se une los resultados. este proceso se repite hasta que todas las sublistas esten ordenadas. 
---

        def prueba_tiempos(n):
* Funcion que evalua el rendimiento del algoritmo
---

        datos = random.sample(range(1, 1000000), n)
* Se generan (n) numeros aleatorios unicos
---

        inicio = time.perf_counter()
        ordenados = quick_sort(datos)
        fin = time.perf_counter()
* Medicion del tiempo 
---

        fin - inicio
* Se calcula el tiempo de ejecucion, que muestra **tamaño de conjuntos de datos , tiempo de ejecucion, primeros 20 valores ordenados.** 

---
# Prueba comparativa
En esta parte del codigo se comparan con diferentes valores de entrada y veanalizar los tiempos de ejecucion del aplicativo.

          tamaños = [2000, 10000, 20000, 40000, 60000, 80000]
* Tamaños de datos
---
        for n in tamaños:
            tiempo = prueba_tiempos(n)
            tiempos.append(tiempo)
* Se almacena el tiempo de ejecucion de la lista(tiempos)
---            
        factor = tiempos[i] / tiempos[i-1]
* Se calcula cuanto aumenta el tiempo al aumentar los datos
---
