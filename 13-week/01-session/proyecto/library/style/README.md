# 📊 Biblioteca de Estilos para Gráficas

Esta carpeta contiene funciones reutilizables para crear gráficas consistentes y profesionales en todo el proyecto.

## 📁 Estructura

```
style/
├── __init__.py          # Módulo principal que exporta todas las funciones
├── graficas.py          # Funciones para crear gráficas
└── README.md            # Este archivo
```

## 🚀 Uso

### 1. Importar la biblioteca en el notebook

```python
import sys
sys.path.append('library')

from style import (
    configurar_estilo_global,
    grafica_barras_aprobados,
    grafica_pastel_aprobados,
    grafica_histograma_notas,
    grafica_barras_por_corte,
    mostrar_estadisticas_tabla,
    guardar_grafica,
    COLORES
)

# Configurar estilo global
configurar_estilo_global()
```

## 📋 Funciones Disponibles

### `configurar_estilo_global()`
Configura el estilo global para todas las gráficas del notebook.

**Uso:**
```python
configurar_estilo_global()
```

---

### `grafica_barras_aprobados(conteo_estado, total_estudiantes, titulo=None, figsize=(10, 6))`
Crea una gráfica de barras mostrando estudiantes aprobados vs no aprobados.

**Parámetros:**
- `conteo_estado`: Series con el conteo de aprobados y no aprobados
- `total_estudiantes`: Número total de estudiantes
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
conteo = df['Estado'].value_counts()
fig, ax = grafica_barras_aprobados(conteo, len(df))
plt.show()
```

---

### `grafica_pastel_aprobados(conteo_estado, titulo=None, figsize=(8, 8))`
Crea una gráfica de pastel mostrando la proporción de aprobados vs no aprobados.

**Parámetros:**
- `conteo_estado`: Series con el conteo de aprobados y no aprobados
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
conteo = df['Estado'].value_counts()
fig, ax = grafica_pastel_aprobados(conteo)
plt.show()
```

---

### `grafica_histograma_notas(df, columna='Nota_Final', bins=10, titulo=None, figsize=(10, 6))`
Crea un histograma de distribución de notas.

**Parámetros:**
- `df`: DataFrame con los datos
- `columna`: Nombre de la columna con las notas
- `bins`: Número de intervalos
- `titulo`: Título personalizado (opcional)
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
fig, ax = grafica_histograma_notas(df, columna='Nota_Final', bins=12)
plt.show()
```

---

### `grafica_barras_por_corte(df, figsize=(12, 6))`
Crea una gráfica de barras agrupadas mostrando las notas por corte de cada estudiante.

**Parámetros:**
- `df`: DataFrame con los datos de estudiantes
- `figsize`: Tamaño de la figura (opcional)

**Retorna:**
- `fig, ax`: Figura y ejes de matplotlib

**Uso:**
```python
fig, ax = grafica_barras_por_corte(df)
plt.show()
```

---

### `mostrar_estadisticas_tabla(df)`
Muestra una tabla con estadísticas descriptivas de las notas.

**Parámetros:**
- `df`: DataFrame con los datos de estudiantes

**Uso:**
```python
mostrar_estadisticas_tabla(df)
```

---

### `guardar_grafica(fig, nombre_archivo, carpeta_output='data/output/img', dpi=300)`
Guarda una gráfica en formato PNG y PDF.

**Parámetros:**
- `fig`: Figura de matplotlib a guardar
- `nombre_archivo`: Nombre del archivo (sin extensión)
- `carpeta_output`: Ruta de la carpeta de salida
- `dpi`: Resolución de la imagen

**Uso:**
```python
fig, ax = grafica_barras_aprobados(conteo, len(df))
guardar_grafica(fig, 'grafica_barras_aprobados')
```

---

## 🎨 Colores Disponibles

La biblioteca define una paleta de colores institucionales:

```python
COLORES = {
    'aprobado': '#2ecc71',      # Verde
    'no_aprobado': '#e74c3c',   # Rojo
    'primario': '#3498db',       # Azul
    'secundario': '#9b59b6',     # Morado
    'advertencia': '#f39c12',    # Naranja
    'info': '#1abc9c',           # Turquesa
    'exito': '#27ae60',          # Verde oscuro
    'peligro': '#c0392b'         # Rojo oscuro
}
```

**Uso:**
```python
plt.plot(x, y, color=COLORES['primario'])
```

## 📝 Ejemplo Completo

```python
# 1. Importar y configurar
import sys
sys.path.append('library')
from style import *
configurar_estilo_global()

# 2. Cargar datos
df = pd.read_csv('data/input/data/notas_estudiante.csv')

# 3. Calcular nota final
df['Nota_Final'] = (df['Corte 1'] * 0.3) + (df['Corte 2'] * 0.3) + (df['Corte 3'] * 0.4)
df['Estado'] = df['Nota_Final'].apply(lambda x: 'Aprobado' if x >= 3.0 else 'No Aprobado')

# 4. Crear gráficas
conteo = df['Estado'].value_counts()

# Barras
fig1, ax1 = grafica_barras_aprobados(conteo, len(df))
guardar_grafica(fig1, 'barras_aprobados')
plt.show()

# Pastel
fig2, ax2 = grafica_pastel_aprobados(conteo)
guardar_grafica(fig2, 'pastel_aprobados')
plt.show()

# Histograma
fig3, ax3 = grafica_histograma_notas(df)
guardar_grafica(fig3, 'histograma_notas')
plt.show()

# Estadísticas
mostrar_estadisticas_tabla(df)
```

## 🔧 Personalización

Todas las funciones permiten personalizar:
- Títulos de las gráficas
- Tamaños de las figuras
- Colores (usando la paleta COLORES)
- Rutas de guardado

## 📦 Dependencias

- `matplotlib`
- `seaborn`
- `pandas`
- `numpy`

## 👨‍💻 Autor

Proyecto Corhuila - 2025
