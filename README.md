# Mutant Detector

## Objetivo del Código

El código proporciona una implementación en Python para detectar si una secuencia de ADN pertenece a un mutante. Un mutante se define como un individuo cuyo ADN presenta secuencias repetidas de al menos cuatro caracteres idénticos, ya sea en filas, columnas o diagonales de una matriz 6x6.

## Funcionamiento Paso a Paso

### 1. Función `is_mutant(dna)`

Esta función toma una matriz `dna` que representa el ADN y verifica si contiene más de una secuencia de cuatro caracteres idénticos en filas, columnas o diagonales. Devuelve `True` si se encuentra un mutante, y `False` en caso contrario.

### 2. Función `ingresar_fila()`

Esta función solicita al usuario ingresar una fila de ADN. Se asegura de que la fila tenga exactamente 6 caracteres y que solo contenga las letras permitidas ('A', 'T', 'C', 'G'). Retorna la fila en forma de lista.

### 3. Función `mostrar_matriz(matriz)`

Muestra en consola la matriz pasada como argumento, formateando las filas.

### 4. Creación de la Matriz de ADN

Se crea una matriz vacía de 6x6 para almacenar el ADN.

```python
dna = [[' ']*6 for _ in range(6)]
```

### 5. Ingreso de Filas de ADN

Se solicita al usuario ingresar cada fila de ADN. La función `ingresar_fila()` se utiliza para validar la entrada.

```python
for i in range(6):
    dna[i] = ingresar_fila()
```
### 6. Mostrar Matriz Resultante
La matriz resultante se muestra en consola utilizando la función `mostrar_matriz()`.

```python
print("\nMatriz Resultante:")
mostrar_matriz(dna)
```
### 7. Verificar Mutación
Se utiliza la función `is_mutant(dna)` para determinar si la matriz de ADN contiene un mutante.

```python
print("\nResultado de la prueba de mutación:")
print("Es mutante" if is_mutant(dna) else "No es mutante")
```

# Cómo Correr el Código

- Abre un entorno de desarrollo Python o ejecuta el código en un entorno de consola.
- Copia y pega el código en un archivo Python (por ejemplo, `mutant_detector.py`).
- Ejecuta el archivo Python.
- El programa solicitará al usuario ingresar cada fila de ADN y mostrará el resultado de la prueba de mutación al final.
- Un ejemplo de un caso mutante es el siguiente `["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]`

### Notas adicionales:

- Asegúrese de proporcionar un código genético válido en el formato de matriz [6x6].