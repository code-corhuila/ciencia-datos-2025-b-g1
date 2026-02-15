# Documento explicativo — Tablero de Ventas (Power BI)

> Archivo creado en Power BI a partir del dataset `DATASET.csv`

---

## 1. Objetivo del tablero

El propósito de este trabajo fue construir un tablero interactivo que permitiera analizar la información de ventas de manera clara, dinámica y útil para la toma de decisiones. A través de Power BI, se desarrollaron diferentes visualizaciones enfocadas en mostrar las **ventas totales**, el **promedio mensual**, el **cumplimiento frente a la meta**, el **Top 5 de productos más vendidos**, los **clientes más frecuentes** y la **evolución de ventas por ciudad y tiempo**.

---

## 2. Preparación del dataset

Inicialmente, cargué el archivo `DATASET.csv` en Power BI mediante la opción *Obtener datos → Texto/CSV*. Luego revisé el tipo de datos de cada columna, asegurándome de que las fechas, montos y textos estuvieran correctamente configurados. Las columnas principales que utilicé fueron:

* `ID_Transaccion`
* `ID_Cliente`
* `Nombre_Cliente`
* `Producto`
* `Ventas_Totales (COP)`
* `Fecha`
* `Mes`
* `Ciudad` o `Región`

También validé que los nombres de las ciudades estuvieran uniformes para evitar errores en el mapa, y formateé la columna de ventas en pesos colombianos (COP).

---

## 3. Creación de medidas DAX

Para el análisis y cálculo de los indicadores, elaboré varias medidas DAX que me permitieron obtener los valores agregados necesarios. A continuación presento las fórmulas utilizadas y su finalidad:

* **Ventas Totales** = `SUM('DATASET'[Ventas_Totales (COP)])`
  Esta medida suma todas las ventas realizadas y representa el valor total facturado.

* **Promedio Mensual** =

  ```DAX
  AVERAGEX(
      VALUES('DATASET'[Mes]),
      CALCULATE(SUM('DATASET'[Ventas_Totales (COP)]))
  )
  ```

  Con esta medida calculé el promedio de ventas mensuales considerando todos los meses del dataset.

* **Meta Ventas** = `[Promedio Mensual] * 1.05`
  Definí la meta mensual como un incremento del 5% sobre el promedio mensual de ventas.

* **Cumplimiento (%)** = `DIVIDE([Ventas Totales], [Meta Ventas], 0)`
  Permite medir el porcentaje de cumplimiento frente a la meta establecida.

* **Clientes Frecuentes** = `COUNT('DATASET'[ID_Transaccion])`
  Mide la cantidad de transacciones por cliente, lo que permite identificar los más activos.

* **Evolución** = `SUM('DATASET'[Ventas_Totales (COP)])`
  Esta medida se usa en los gráficos de líneas para mostrar cómo cambian las ventas a lo largo del tiempo.

Además, para mejorar el análisis, agregué una columna calculada `MesAño = FORMAT([Fecha], "YYYY-MM")` que facilitó el seguimiento temporal.

---

## 4. Solución al problema del mapa

Durante la creación del mapa, Power BI no reconocía algunas ciudades. Para solucionarlo:

1. Asigné la **categoría de datos** de la columna `Ciudad` como *Ciudad* (City) en el panel de modelado.
2. Agregué una columna `País` con el valor *Colombia*, para que Bing Maps pudiera ubicar correctamente las ciudades.
3. Uniformicé los nombres (por ejemplo, aseguré que “Bogotá” tuviera tilde en todas las filas).
4. Probé el uso de un **Mapa de burbujas** con los campos: `Ciudad` como ubicación y `SUM(Ventas_Totales (COP))` como tamaño de burbuja.

Después de estos ajustes, el mapa empezó a reconocer todas las regiones correctamente.

---

## 5. Diseño del tablero

El tablero se organizó de la siguiente forma:

* En la parte superior se colocaron los **indicadores KPI**: Ventas Totales, Promedio Mensual, Cumplimiento (%) y Meta.
* En la parte media incluí dos gráficos de barras horizontales: uno para los **Top 5 productos más vendidos** y otro para los **Clientes más frecuentes**.
* En la parte inferior añadí un **gráfico de líneas** que muestra la evolución de las ventas por mes y ciudad, y un **mapa geográfico** que refleja la distribución de ventas en Colombia.
* Los colores y diseño se mantuvieron uniformes en tonos rosados y blancos, para dar coherencia visual y resaltar los KPIs.

---

## 6. Justificación de las decisiones visuales

* Los **KPI** se ubicaron en la parte superior para ofrecer una visión rápida del rendimiento general.
* El **Top 5 de productos** facilita identificar los artículos que generan mayores ingresos.
* El gráfico de **Clientes frecuentes** permite reconocer los compradores con más transacciones y priorizar estrategias de fidelización.
* La **serie temporal** ayuda a detectar tendencias, picos y caídas en las ventas mensuales.
* El **mapa** brinda una visión geográfica de la distribución de las ventas, útil para decisiones de cobertura y logística.

---

## 7. Pasos realizados en Power BI

1. Cargué y transformé el dataset desde el archivo CSV.
2. Validé los tipos de datos y eliminé duplicados.
3. Creé las medidas DAX indicadas.
4. Diseñé los visuales según las métricas clave.
5. Apliqué formato a las cifras (moneda COP, porcentaje, miles).
6. Organicé el tablero priorizando claridad y lectura rápida.
7. Verifiqué la interactividad entre los gráficos.

---

## 8. Conclusiones y recomendaciones

El tablero permite tener una vista general del comportamiento de las ventas, identificar productos clave y monitorear el cumplimiento frente a la meta. Gracias al mapa, se pueden visualizar las ciudades con mayor contribución, lo que es útil para definir estrategias comerciales regionales.

Como mejora futura, se podría incorporar una tabla de fechas para análisis más detallado por año y trimestre, además de integrar márgenes o costos para obtener indicadores de rentabilidad.

