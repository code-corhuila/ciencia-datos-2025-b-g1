# 📚 Biblioteca del Proyecto

Esta carpeta contiene funciones genéricas y reutilizables para el proyecto de análisis de notas estudiantiles.

## 📁 Estructura

```
library/
├── README.MD          # Este archivo
└── style/             # Módulo de estilos para gráficas
    ├── __init__.py
    ├── graficas.py
    └── README.md
```

## 🎨 Módulo `style`

El módulo `style` contiene funciones reutilizables para crear gráficas consistentes y profesionales.

### Funciones Principales:

- **`configurar_estilo_global()`**: Configura el estilo global de todas las gráficas
- **`grafica_barras_aprobados()`**: Gráfica de barras de aprobados vs no aprobados
- **`grafica_pastel_aprobados()`**: Gráfica de pastel de proporción de aprobados
- **`grafica_histograma_notas()`**: Histograma de distribución de notas
- **`grafica_barras_por_corte()`**: Barras agrupadas por corte
- **`mostrar_estadisticas_tabla()`**: Muestra estadísticas descriptivas
- **`guardar_grafica()`**: Guarda gráficas en PNG y PDF

### Uso Rápido:

```python
import sys
sys.path.append('library')

from style import *

# Configurar estilos
configurar_estilo_global()

# Usar funciones
fig, ax = grafica_barras_aprobados(conteo_estado, total_estudiantes)
plt.show()
```

Para más detalles, consulta: [`style/README.md`](style/README.md)

## 🔧 Agregar Nuevas Funciones

Para agregar nuevas funciones genéricas:

1. Crea un nuevo archivo `.py` en la carpeta correspondiente
2. Define tus funciones con documentación clara
3. Actualiza el `__init__.py` para exportar las funciones
4. Documenta el uso en el README correspondiente

## 📝 Convenciones

- Todas las funciones deben tener docstrings
- Usar type hints cuando sea posible
- Mantener la consistencia de estilo (PEP 8)
- Documentar parámetros y valores de retorno

---

**Proyecto Corhuila - Ciencia de Datos 2025**