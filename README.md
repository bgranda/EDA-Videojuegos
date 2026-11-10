# Historia de los Videojuegos: de los 8 bits al 4K (1980 – 2020)

Análisis Exploratorio de Datos (EDA) sobre las ventas de videojuegos a nivel mundial entre 1980 y 2020. El proyecto estudia cómo ha evolucionado el mercado, cuáles son los títulos superventas, qué consolas y fabricantes dominan el sector y cómo cambian las preferencias de género según la época y la región.

## 👤 Autor

El proyecto está realizado por Beatriz Granda Arroyo.

## 🎯 Objetivo

Entender el comportamiento del mercado de los videojuegos a lo largo de cuatro décadas, identificando tendencias de ventas, diferencias regionales y el posicionamiento de los principales fabricantes de consolas.

## 💡 Hipótesis

1. Las ventas de videojuegos han variado de forma significativa con el tiempo.
2. Existen unos pocos videojuegos superventas que concentran gran parte del mercado.
3. Hay consolas claramente más populares que otras.
4. Existe un fabricante de consolas líder en el sector.
5. Hay géneros de videojuegos que se venden más que otros.
6. Los géneros más vendidos dependen del fabricante de la consola.

## 📊 Datos

Los datos se obtuvieron de **Kaggle**, a partir de 7 archivos de distintas fuentes. Tras la limpieza se generó un único archivo final: `videojuegos.csv`.

## 🔍 Metodología

1. **Recogida y visualización de datos.** Se descargaron 7 archivos de Kaggle. Uno de ellos se descartó porque su forma de recoger los datos difería del resto.
2. **Limpieza de datos.** Se eliminaron las columnas que no aportaban información al análisis, se homogeneizaron los tipos de datos y se ordenaron los archivos. Se detectaron dos archivos idénticos y se eliminó uno. Finalmente, se unieron todos en `videojuegos.csv`.
3. **Planteamiento de hipótesis.**
4. **Análisis exploratorio**, organizado en cinco bloques:
   - 4.1 Evolución de las ventas y de los géneros por época (1980–1999 vs. 2000–2020) y por región
   - 4.2 Videojuegos más vendidos (superventas) y curva de Pareto
   - 4.3 Consolas más populares a nivel global y por región
   - 4.4 Fabricantes de consolas líderes
   - 4.5 Géneros vendidos por cada fabricante

## 📈 Principales resultados

### 1. Evolución de los videojuegos

A partir del año 2000 se produce una revolución en el sector, impulsada por el desarrollo tecnológico de las consolas y la mejora de la conexión a internet. Las ventas crecen de forma notable en casi todos los géneros y aparecen géneros nuevos como *Action-Adventure*.

También cambian las preferencias: entre 1980 y 1999 dominaban los juegos de **Plataformas** y **Rol**, mientras que entre 2000 y 2020 lideran **Acción**, **Deportes** y **Disparos**. Por regiones, Norteamérica, Europa y el resto del mundo siguen esta misma tendencia, pero **Japón mantiene su preferencia por el Rol**.

### 2. Superventas

- **Call of Duty** es la franquicia con más presencia en el Top 20 mundial.
- Norteamérica y Europa tienen gustos similares (Wii Sports, GTA V, Call of Duty), aunque en Norteamérica destaca *Super Mario Bros.* y en Europa la saga *FIFA*.
- Japón es muy diferente: lideran *New Super Mario Bros.*, *Pokémon* y *Animal Crossing*.
- Casi la mitad de los registros son títulos repetidos, ya que un mismo videojuego se vende para varias consolas, por lo que las ventas se agregaron por título.

**Curva de Pareto:** el **80 % de las ventas globales se concentra en solo el 16 % de los videojuegos**. El mercado está dominado por un grupo reducido de superventas.

### 3. Consolas

- **Norteamérica:** mismas preferencias que a nivel global (X360, Wii, PS3).
- **Europa:** PS3 y Wii, con PS4 por delante de X360.
- **Japón:** dominan las portátiles de Nintendo (DS y 3DS).
- **Resto del mundo:** destacan PS3, PS2 y PS4.

### 4. Fabricantes

Aunque la X360 está entre las consolas más vendidas, el mercado por fabricante lo dominan claramente **Sony y Nintendo**, tanto a nivel global como por regiones. Nintendo lidera en Norteamérica y Japón; Sony en Europa y el resto del mundo.

### 5. Géneros por fabricante

- **Sony:** fuertemente concentrado en **Acción**, seguido de Deportes y Disparos.
- **Nintendo:** reparto más equilibrado entre Plataformas, Miscelánea, Deportes, Acción y Rol.
- **Microsoft:** centrado en **Disparos** y Acción.

En Japón, el género más vendido es el **Rol de Nintendo**, a diferencia del resto de regiones, donde lidera la **Acción de Sony**.

## ✅ Conclusiones

- Desde el año 2000 se produce un gran cambio en la industria: aumentan mucho las ventas y cambian los géneros más jugados.
- Las ventas están influenciadas porque un mismo videojuego se lanza para varias consolas.
- El 80 % de las ventas se concentra en solo el 16 % de los videojuegos.
- Los videojuegos más vendidos a nivel mundial y por regiones coinciden, **excepto en Japón**.
- Las consolas más populares son **PS3, X360 y Wii**.
- Los fabricantes líderes son **Sony y Nintendo**.
- Sony vende principalmente Acción, Deportes y Disparos; Nintendo reparte sus ventas de forma equitativa entre varios géneros.

## 🛠️ Tecnologías

- **Lenguaje y entorno:** Python 3 y Jupyter Notebook
- **Tratamiento de datos:** [pandas](https://pandas.pydata.org/) y [NumPy](https://numpy.org/)
- **Visualización estática:** [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) y [squarify](https://github.com/laserson/squarify) (treemaps)
- **Visualización interactiva:** [Plotly](https://plotly.com/python/) (Plotly Express, Graph Objects y `make_subplots`) para treemaps y gráficos interactivos

