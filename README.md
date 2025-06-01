# Análisis de Tendencias Turísticas en Europa 2023

## 1. Introducción

Este proyecto corresponde al caso de estudio asignado en la Unidad 2 de la asignatura “Visualización de Toma de Decisiones” de la Institución Universitaria Digital de Antioquia (UDigital). El propósito es analizar las tendencias de viajes en Europa durante el año 2023, con el fin de que una agencia de turismo mejore sus ofertas y estrategias de marketing. A partir de un conjunto de datos en formato CSV/Excel, se exploran distintos aspectos clave de la actividad turística a través de visualizaciones que faciliten la toma de decisiones.

## 2. Objetivos

1. **Identificar patrones estacionales de viaje**  
   Comprender cuáles son los meses con mayor y menor cantidad de viajes para reconocer temporadas altas y bajas.

2. **Determinar los destinos más populares**  
   Detectar las ciudades con mayor número de visitas durante 2023.

3. **Analizar la relación entre tipo de alojamiento y gasto diario**  
   Observar cómo varía el gasto promedio según el tipo de alojamiento utilizado por los viajeros.

4. **Evaluar la satisfacción del cliente por país**  
   Visualizar la distribución de las valoraciones de los clientes, por país, para medir niveles de satisfacción.

5. **Calcular la duración promedio de estancia por destino**  
   Identificar qué ciudades o países presentaron estancias más prolongadas en promedio.

6. **Visualizar la distribución geográfica de los viajes**  
   Mapa interactivo que muestre la ubicación de cada viaje, codificando país (color) y duración de estancia (tamaño de punto).

## 3. Contenido del Repositorio

```
EA2/
├── data/
│   └── dataset.csv                  # Conjunto de datos de viajes en Europa 2023
├── docs/
│   ├── average_expense_by_accommodation.png
│   ├── average_rating_by_accommodation.png
│   ├── average_rating_by_country.png
│   ├── average_stay_by_city.png
│   ├── longest_stays_by_country.png
│   ├── most_popular_months.png
│   ├── most_visited_cities.png
│   └── geo_distribution_map.html   # Mapa interactivo de distribución geográfica
├── src/
│   ├── application/                 # Casos de uso (Use Cases)
│   │   ├── accommodation/
│   │   │   ├── get_average_expense_by_accommodation_use_case.py
│   │   │   ├── get_average_rating_by_accommodation_use_case.py
│   │   │   └── get_expense_boxplot_by_accommodation_type_use_case.py
│   │   ├── destination/
│   │   │   ├── get_average_stay_by_city_use_case.py
│   │   │   ├── get_longest_stays_by_destination_use_case.py
│   │   │   └── get_most_visited_cities_use_case.py
│   │   ├── satisfaction/
│   │   │   ├── get_average_rating_by_country_use_case.py
│   │   │   └── get_rating_boxplot_by_country_use_case.py
│   │   └── trip/
│   │       ├── get_most_popular_months_use_case.py
│   │       └── get_travel_geo_distribution_use_case.py
│   ├── domain/                      # Modelos de dominio e interfaces (Gateways)
│   │   └── model/
│   │       ├── accommodation/
│   │       │   ├── accommodation.py
│   │       │   └── gateways/
│   │       │       ├── get_average_expense_by_accommodation.py
│   │       │       ├── get_average_rating_by_accommodation.py
│   │       │       └── get_expense_boxplot_by_accommodation_type.py
│   │       ├── destination/
│   │       │   ├── destination.py
│   │       │   └── gateways/
│   │       │       ├── get_average_stay_by_city.py
│   │       │       ├── get_longest_stays_by_destination.py
│   │       │       └── get_most_visited_cities.py
│   │       ├── satisfaction/
│   │       │   ├── satisfaction.py
│   │       │   └── gateways/
│   │       │       ├── get_average_rating_by_country.py
│   │       │       └── get_rating_boxplot_by_country.py
│   │       └── trip/
│   │           ├── trip.py
│   │           └── gateways/
│   │               ├── get_most_popular_months.py
│   │               └── get_travel_geo_distribution.py
│   ├── infrastructure/              # Implementaciones concretas (acceso a CSV)
│   │   ├── accommodation/
│   │   │   ├── get_average_expense_by_accommodation_csv.py
│   │   │   ├── get_average_rating_by_accommodation_csv.py
│   │   │   └── get_expense_boxplot_by_accommodation_type_csv.py
│   │   ├── destination/
│   │   │   ├── get_average_stay_by_city_csv.py
│   │   │   ├── get_longest_stays_by_destination_csv.py
│   │   │   └── get_most_visited_cities_csv.py
│   │   ├── satisfaction/
│   │   │   ├── get_average_rating_by_country_csv.py
│   │   │   └── get_rating_boxplot_by_country_csv.py
│   │   └── trip/
│   │       ├── get_most_popular_months_csv.py
│   │       └── get_travel_geo_distribution_csv.py
│   ├── main.py                       # Orquestador que ejecuta todos los casos de uso
│   └── test.ipynb                    # Notebook de prueba (antes de dashboard final)
├── README.md                         # Este documento
└── requirements.txt                  # Dependencias del proyecto
```

## 4. Descripción del Dataset

El archivo `data/dataset.csv` contiene un registro de los viajes realizados por turistas en Europa durante 2023. Cada fila representa un viaje individual y, entre sus columnas principales, se incluyen:

- **id_viaje**: Identificador único de cada viaje.  
- **fecha_inicio** / **fecha_fin**: Fechas de inicio y fin de la estancia.  
- **mes**: Mes en el que se realizó el viaje (1–12).  
- **pais**: País de destino.  
- **ciudad**: Ciudad de destino.  
- **tipo_alojamiento**: Clasificación del alojamiento (por ejemplo, hotel, hostal, apartamento).  
- **gasto_diario**: Gasto promedio diario (en moneda local).  
- **valoracion_cliente**: Calificación de satisfacción otorgada por el cliente (escala del 1 al 5).  
- **latitud** / **longitud**: Coordenadas geográficas de la ubicación del viaje (para visualización en mapa).  

> **Nota:** Se recomienda revisar la primera línea (cabeceras) para confirmar nombres exactos de columnas antes de ejecutar cualquier caso de uso.

## 5. Estructura de Casos de Uso y Repositorios

El proyecto sigue un enfoque de Arquitectura Limpia (Clean Architecture) unido a principios SOLID y Domain-Driven Design (DDD). En `src/application` se ubican los casos de uso (use cases) que implementan la lógica de negocio, mientras que en `src/infrastructure` están las implementaciones concretas de lectura de CSV. Cada caso de uso se alimenta de un repositorio que cumple con la interfaz definida en `src/domain/model/.../gateways`.

Por ejemplo, para la funcionalidad de “Patrones estacionales de viaje”:

1. **Interfaz de dominio**  
   `src/domain/model/trip/gateways/get_most_popular_months.py` define el método `execute()` que retorna un diccionario `{mes: cantidad_de_viajes}`.

2. **Implementación CSV**  
   `src/infrastructure/trip/get_most_popular_months_csv.py` implementa la interfaz anterior. Lee el CSV, calcula el conteo de viajes por mes y genera un archivo gráfico `most_popular_months.png` en `docs/`.

3. **Caso de uso**  
   `src/application/trip/get_most_popular_months_use_case.py` recibe el repositorio en el constructor y, en su método `execute()`, invoca al repositorio para que realice la operación.

4. **Orquestador**  
   `src/main.py` crea instancias de cada repositorio e inyecta dichas dependencias en los casos de uso, luego ejecuta todos los casos de uso y muestra por consola las salidas tabulares (cuando aplica) y/o genera los archivos en `docs/`.

Este patrón se repite para cada una de las seis visualizaciones solicitadas.

## 6. Descripción de Visualizaciones

1. **Patrones estacionales de viaje**  
   - **Archivo generado**: `docs/most_popular_months.png`  
   - **Descripción**: Gráfico de barras vertical que muestra la cantidad de viajes por cada mes del año 2023, permitiendo identificar temporadas altas y bajas.

2. **Destinos más populares**  
   - **Archivo generado**: `docs/most_visited_cities.png`  
   - **Descripción**: Gráfico de barras horizontales con las 10 ciudades más visitadas, ordenadas de mayor a menor.

3. **Relación entre tipo de alojamiento y gasto diario**  
   - **Archivos generados**:  
     - `docs/expense_boxplot_by_accommodation_type.png`  
   - **Descripción**: Diagrama de caja (boxplot) que ilustra la distribución del gasto diario según cada tipo de alojamiento.

4. **Satisfacción del cliente por país**  
   - **Archivos generados**:  
     - `docs/rating_boxplot_by_country.html` (interactivo)  
     - `docs/rating_boxplot_by_country.png` (estático, en caso de visualizar sin HTML)  
   - **Descripción**: Diagrama de caja interactivo que muestra la distribución de valoraciones de clientes agrupadas por país. El archivo HTML permite filtrar, hacer hover y descargar la figura.

5. **Duración promedio de estancia por destino**  
   - **Visualización interactiva en Notebook**:  
     - Se genera dinámicamente mediante Plotly en el notebook.  
   - **Descripción**: Gráfico de barras interactivo que expone la duración promedio de cada estancia (en días) para cada ciudad. Permite ordenar, hacer zoom y descargar la gráfica.

6. **Distribución geográfica de los viajes**  
   - **Archivo generado**: `docs/geo_distribution_map.html`  
   - **Descripción**: Mapa interactivo (usando Plotly/Mapbox) en el que cada punto representa un viaje. El color codifica el país de destino y el tamaño del punto la duración de la estancia. Se proporciona tanto el HTML para interacción completa como un vistazo estático en el Notebook.

> **Insight generales extraídos**  
> - Identificación de meses con mayor demanda turística.  
> - Detección de los destinos más frecuentados.  
> - Comparación del gasto diario según tipo de alojamiento.  
> - Niveles de satisfacción de clientes desagregados por país.  
> - Destinos que registraron estancias más largas.  
> - Distribución espacial de los viajes en el mapa.

## 7. Requisitos e Instalación

1. **Entorno de Python 3.10+**  
   Asegúrese de tener Python 3.10 o superior instalado.

2. **Dependencias**  
   Desde la carpeta raíz del proyecto (`EA2/`), ejecute:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` contiene, como mínimo:
   ```
   pandas
   matplotlib
   seaborn
   plotly
   nbformat
   ```

3. **Estructura de carpetas**  
   - `data/dataset.csv`: Conjunto de datos en formato CSV exportado desde Excel.  
   - `docs/`: Carpeta donde se guardan las imágenes PNG y archivos HTML generados.  
   - `src/`: Código fuente dividido en los módulos `application`, `domain` e `infrastructure`.  
   - `src/main.py`: Script principal que genera todas las visualizaciones.  
   - `dashboard_trends_europe_2023.ipynb`: Notebook interactivo para producir y visualizar las gráficas en Jupyter.  

## 8. Ejecución del Proyecto

### 8.1. Generar visualizaciones desde consola

Desde la carpeta `EA2/`, ejecute:

```bash
python src/main.py
```

- Cada uno de los seis casos de uso leerá `data/dataset.csv` y generará su respectivo archivo de salida en `docs/`.  
- Se mostrará información resumida en consola (p.ej., tablas de resultados).

### 8.2. Usar el Notebook interactivo

1. Abra Jupyter Notebook o JupyterLab en la raíz del proyecto:
   ```bash
   jupyter notebook
   ```
2. Localice y abra `dashboard_trends_europe_2023.ipynb`.  
3. Ejecute todas las celdas en orden:
   - La sección de “Configuración e importaciones” ajusta rutas e importa los casos de uso.  
   - La celda “Generar todas las visualizaciones” invoca a `main.py`.  
   - Cada subsección muestra las imágenes estáticas o incrusta los archivos HTML para las visualizaciones interactivas.

**Nota**: Si la ruta al dataset o a los archivos HTML varía, modifique las celdas de configuración en el notebook para apuntar correctamente a `data/dataset.csv` y `docs/geo_distribution_map.html`.

## 9. Estructura del Notebook

1. **Título y descripción del caso de estudio**  
2. **Configuración e importaciones**  
3. **Ejecución del script principal (`main.py`)**  
4. **Sección: Patrones estacionales de viaje**  
5. **Sección: Destinos más populares**  
6. **Sección: Relación entre tipo de alojamiento y gasto diario**  
7. **Sección: Satisfacción del cliente por país (interactivo)**  
8. **Sección: Duración promedio de estancia por destino (interactivo)**  
9. **Sección: Distribución geográfica de los viajes (mapa interactivo)**  
10. **Sección adicional para visualizar archivo HTML local de mapa**  


## 10. Conclusiones

A través de las seis visualizaciones solicitadas, este proyecto permite:

- Reconocer las épocas del año con mayor afluencia turística.  
- Identificar las ciudades más atractivas para los visitantes en 2023.  
- Comprender cómo varía el gasto de los turistas según el tipo de alojamiento.  
- Evaluar la satisfacción promedio por país y concluir en estrategias de mejora.  
- Determinar destinos que fomentan estancias más prolongadas y, por ende, mayores ingresos.  
- Apreciar la distribución geográfica de los viajes en un mapa interactivo, esencial para la planificación geoestratégica.

Cada uno de estos análisis resulta valioso para la toma de decisiones en marketing y planificación de ofertas, tanto para la agencia de turismo como para posibles aliados y operadores turísticos en Europa.

## 11. Licencia

**CC BY NC – Institución Universitaria Digital de Antioquia (UDigital)**  
Esta licencia permite a terceros distribuir, remezclar, retocar y crear obras derivadas de manera no comercial. Es obligatorio mencionar a la Institución Universitaria Digital de Antioquia y mantener el carácter no comercial en cualquier obra derivada. No es obligatorio licenciar las obras resultantes bajo las mismas condiciones.

> Institución Universitaria Digital de Antioquia – www.ludigital.edu.co
