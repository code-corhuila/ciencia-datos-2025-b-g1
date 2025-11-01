"""
Biblioteca de estilos para el proyecto de análisis de notas
"""

from .graficas import (
    configurar_estilo_global,
    grafica_barras_aprobados,
    grafica_pastel_aprobados,
    grafica_histograma_notas,
    grafica_barras_por_corte,
    mostrar_estadisticas_tabla,
    guardar_grafica,
    COLORES
)

__all__ = [
    'configurar_estilo_global',
    'grafica_barras_aprobados',
    'grafica_pastel_aprobados',
    'grafica_histograma_notas',
    'grafica_barras_por_corte',
    'mostrar_estadisticas_tabla',
    'guardar_grafica',
    'COLORES'
]
